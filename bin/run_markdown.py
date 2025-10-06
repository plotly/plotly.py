#!/usr/bin/env python3
"""
Process Markdown files with embedded Python code blocks, saving
the output.
"""

import argparse
from contextlib import redirect_stdout, redirect_stderr
import io
from pathlib import Path
import plotly.graph_objects as go
import re
import sys
import traceback


def main():
    args = _parse_args()
    if args.block is None:
        for filename in args.inputs:
            _do_file(args, Path(filename))
    else:
        _do_file(args, Path(args.inputs[0]), block_number=args.block)


def _do_file(args, input_file, block_number=None):
    """Process a single file."""

    # Validate input file
    if not input_file.exists():
        print(f"Error: '{input_file}' not found", file=sys.stderr)
        sys.exit(1)

    # Determine output file path etc.
    stem = input_file.stem
    output_file = args.outdir / f"{input_file.stem}{input_file.suffix}"
    
    if input_file.resolve() == output_file.resolve():
        print(f"Error: output would overwrite input '{input_file}'", file=sys.stderr)
        sys.exit(1)

    # Read input
    try:
        with open(input_file, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading input file: {e}", file=sys.stderr)
        sys.exit(1)

    # Parse markdown and extract code blocks
    _report(args.verbose > 0, f"Processing {input_file}...")
    code_blocks = _parse_md(content)
    _report(args.verbose > 1, f"- Found {len(code_blocks)} code blocks")

    # Execute code blocks and collect results
    execution_results = _run_all_blocks(args, input_file, code_blocks, stem, block_number)
    if block_number is not None:
        return

    # Generate and save output
    content = _generate_markdown(args, content, code_blocks, execution_results, args.outdir)
    try:
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(content)
        _report(args.verbose > 1, f"- Output written to {output_file}")
    except Exception as e:
        print(f"Error writing output file: {e}", file=sys.stderr)
        sys.exit(1)

def _contains_latex(code):
    """Check if code likely contains LaTeX expressions."""
    return "cdn" if '$' in code and re.search(r'\$[^$]+\$', code) else False

def _capture_plotly_show(fig, counter, result, output_dir, stem, mathjax_option):
    """Saves HTML figures."""
    # Save HTML and get the content for embedding
    html_filename = f"{stem}_{counter}.html"
    html_path = output_dir / html_filename
    fig.write_html(html_path, include_plotlyjs="cdn", include_mathjax=mathjax_option)
    html_content = fig.to_html(include_plotlyjs="cdn", include_mathjax=mathjax_option, div_id=f"plotly-div-{counter}", full_html=False)
    result["html_files"].append(html_filename)
    result.setdefault("html_content", []).append(html_content)


def _generate_markdown(args, content, code_blocks, execution_results, output_dir):
    """Generate the output markdown with embedded results."""
    lines = content.split("\n")

    # Sort code blocks by start line in reverse order for safe insertion
    sorted_blocks = sorted(
        enumerate(code_blocks), key=lambda x: x[1]["start_line"], reverse=True
    )

    # Process each code block and insert results
    for block_idx, block in sorted_blocks:
        result = execution_results[block_idx]
        insert_lines = []

        # Add output if there's stdout
        if result["stdout"].strip():
            insert_lines.append("")
            insert_lines.append("**Output:**")
            insert_lines.append("```")
            insert_lines.extend(result["stdout"].rstrip().split("\n"))
            insert_lines.append("```")

        # Add error if there was one
        if result["error"]:
            insert_lines.append("")
            insert_lines.append("**Error:**")
            insert_lines.append("```")
            insert_lines.extend(result["error"].rstrip().split("\n"))
            insert_lines.append("```")

        # Add stderr if there's content
        if result["stderr"].strip():
            insert_lines.append("")
            insert_lines.append("**Warnings/Messages:**")
            insert_lines.append("```")
            insert_lines.extend(result["stderr"].rstrip().split("\n"))
            insert_lines.append("```")

        # Embed HTML content for plotly figures
        if args.inline:
            for html_content in result.get("html_content", []):
                insert_lines.extend(html_content.split("\n"))

        # Insert the results after the code block
        if insert_lines:
            # Insert after the closing ``` of the code block
            insertion_point = block["end_line"] + 1
            lines[insertion_point:insertion_point] = insert_lines

    return "\n".join(lines)


def _parse_args():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description="Process Markdown files with code blocks")
    parser.add_argument("inputs", nargs="+", help="Input .md files")
    parser.add_argument("--block", type=int, help="Single block to run")
    parser.add_argument("--inline", action="store_true", help="Inline HTML in .md")
    parser.add_argument("--outdir", type=Path, help="Output directory for MD files")
    parser.add_argument("--htmldir", type=Path, help="Output directory for HTML files")
    parser.add_argument("--verbose", type=int, default=0, help="Integer verbosity level")
    return parser.parse_args()


def _parse_md(content):
    """Parse Markdown and extract Python code blocks."""
    lines = content.split("\n")
    blocks = []
    current_block = None
    in_code_block = False
    in_region_block = False

    for i, line in enumerate(lines):
        # Check for region start/end markers
        if "<!-- #region" in line:
            in_region_block = True
        elif "<!-- #endregion" in line:
            in_region_block = False
            
        # Start of Python code block
        elif line.strip().startswith("```python"):
            # Only process code blocks that are NOT inside region blocks
            if not in_region_block:
                in_code_block = True
                current_block = {
                    "start_line": i,
                    "end_line": None,
                    "code": [],
                    "type": "python",
                }

        # End of code block
        elif line.strip() == "```" and in_code_block:
            in_code_block = False
            current_block["end_line"] = i
            current_block["code"] = "\n".join(current_block["code"])
            blocks.append(current_block)
            current_block = None

        # Line inside code block
        elif in_code_block:
            current_block["code"].append(line)

    return blocks


def _report(condition, message):
    """Report if condition is true."""
    if condition:
        print(message, file=sys.stderr)


def _run_all_blocks(args, input_file, code_blocks, stem=None, block_number=None):
    """Run blocks found in a file."""
    execution_results = []
    env = {
            "__name__": "__main__",
            "__file__": "<markdown_code>",
        }
    figure_counter = 0
    for i, block in enumerate(code_blocks):
        if block_number is None:
            _report(args.verbose > 1, f"- Executing block {i}/{len(code_blocks)}")
            figure_counter, result = _run_code(block["code"], args.htmldir, figure_counter, stem, env)
            execution_results.append(result)
            _report(args.verbose > 0 and bool(result["error"]), f"  - Warning: block {i} had an error in {input_file}")
        elif block_number == i:
            print(f"block number {block_number}")
            figure_counter, result = _run_code(block["code"], args.htmldir, figure_counter, stem)
            print("--- standard output")
            print(result["stdout"])
            print("--- standard error")
            print(result["stderr"])
    return execution_results


def _run_code(code, output_dir, figure_counter, stem, exec_globals):
    """Execute code capturing output and generated files."""
    mathjax_option = _contains_latex(code)
    
    # Capture stdout and stderr
    stdout_buffer = io.StringIO()
    stderr_buffer = io.StringIO()

    # Track files created during execution
    if not output_dir.exists():
        output_dir.mkdir(parents=True, exist_ok=True)

    files_before = set(f.name for f in output_dir.iterdir())
    result = {"stdout": "", "stderr": "", "error": None, "html_files": []}
    try:

        # Create a namespace for code execution
        # exec_globals = {
        #     "__name__": "__main__",
        #     "__file__": "<markdown_code>",
        # }

        # Execute the code with output capture
        with redirect_stdout(stdout_buffer), redirect_stderr(stderr_buffer):
            # Try to import plotly and patch the show method
            def patched_show(self, *args, **kwargs):
                nonlocal figure_counter
                figure_counter += 1
                if stem is not None:
                    _capture_plotly_show(self, figure_counter, result, output_dir, stem, mathjax_option)
            original_show = go.Figure.show
            go.Figure.show = patched_show
            exec(code, exec_globals)
            go.Figure.show = original_show

    except Exception as e:
        result["error"] = f"Error executing code: {str(e)}\n{traceback.format_exc()}"

    result["stdout"] = stdout_buffer.getvalue()
    result["stderr"] = stderr_buffer.getvalue()

    # File tracking removed - no files are generated

    return figure_counter, result


if __name__ == "__main__":
    main()
