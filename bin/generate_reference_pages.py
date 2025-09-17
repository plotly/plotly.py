"""Generate the code reference pages and navigation."""

import os
from pathlib import Path

import mkdocs_gen_files

OUTPUT_ROOT = Path("reference")
SUMMARY_FILE = Path("SUMMARY.md")
INDEX_FILE = "index.md"

SKIP_DIR = "graph_objects"

CONTENT = """
# {title}

::: {ident}
"""


def main():
    """Main driver."""

    # Setup.
    temp_dir = _get_temp_dir()
    nav = mkdocs_gen_files.Nav()

    # Process each Python file.
    for path in sorted(Path("plotly").rglob("*.py")):
        if _skip_file(path):
            continue

        # Paths.
        module_path = path.relative_to(".").with_suffix("")
        doc_path = path.relative_to(".").with_suffix(".md")
        full_doc_path = OUTPUT_ROOT / doc_path

        # Dunder special cases.
        parts = tuple(module_path.parts)
        if parts[-1] == "__main__":
            continue
        if parts[-1] == "__init__":
            parts = parts[:-1]
            doc_path = doc_path.with_name(INDEX_FILE)
            full_doc_path = full_doc_path.with_name(INDEX_FILE)

        # Save constructed data.
        nav[parts] = doc_path.as_posix()
        mkdocs_gen_files.set_edit_path(full_doc_path, path)
        content = _make_content(parts)
        _save_in_memory(full_doc_path, content)
        _save_in_temp_dir(temp_dir, doc_path, content)

    # Generate navigation summary.
    _generate_nav_summary(temp_dir, nav)


def _generate_nav_summary(temp_dir, nav):
    """Create navigation summary (saving if requested)."""
    lines = nav.build_literate_nav()

    with mkdocs_gen_files.open(OUTPUT_ROOT / SUMMARY_FILE, "w") as writer:
        writer.writelines(lines)

    if temp_dir is not None:
        with open(temp_dir / SUMMARY_FILE, "w") as writer:
            writer.writelines(lines)


def _get_temp_dir():
    """Get temporary directory for on-disk files if requested."""
    temp_dir = os.getenv("MKDOCS_TEMP_DIR", None)
    if temp_dir is not None:
        temp_dir = Path(temp_dir)
    return temp_dir


def _make_content(parts):
    """Generate text to put in files."""
    ident = parts
    if (len(parts) == 3) and (parts[1] == SKIP_DIR) and (parts[2] != SKIP_DIR):
        ident = [*parts[:-1], f"_{parts[2]}"]
    return CONTENT.format(title=".".join(parts), ident=".".join(ident))


def _save_in_memory(output_path, content):
    """Save in-memory file."""
    with mkdocs_gen_files.open(output_path, "w") as writer:
        writer.write(content)


def _save_in_temp_dir(temp_dir, doc_path, content):
    """Save on-disk file."""
    if temp_dir is None:
        return

    temp_path = temp_dir / doc_path
    temp_path.parent.mkdir(exist_ok=True, parents=True)
    with open(temp_path, "w") as writer:
        writer.write(content)


def _skip_file(path):
    """Don't include files like 'graph_objects/_bar.py'."""
    return (
        path.is_file() and (path.parent.name == SKIP_DIR) and str(path.name).startswith("_")
    )


# Do NOT protect this with `if __name__ == "__main__"` because this is
# run as a plugin by MkDocs rather than as a top-level script.
main()
