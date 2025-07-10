"""Generate the code reference pages and navigation."""

import os
from pathlib import Path

import mkdocs_gen_files


# Saving Markdown files?
temp_dir = os.getenv("MKDOCS_TEMP_DIR", None)
if temp_dir is not None:
    temp_dir = Path(temp_dir)

# Set up the generation engine.
nav = mkdocs_gen_files.Nav()

# Match each Python file.
for path in sorted(Path("plotly").rglob("*.py")):
    # Documentation path.
    module_path = path.relative_to(".").with_suffix("")
    doc_path = path.relative_to(".").with_suffix(".md")
    full_doc_path = Path("reference", doc_path)

    # Handle dunder special cases.
    parts = tuple(module_path.parts)
    if parts[-1] == "__init__":
        parts = parts[:-1]
        doc_path = doc_path.with_name("index.md")
        full_doc_path = full_doc_path.with_name("index.md")
    elif parts[-1] == "__main__":
        continue

    # Save constructed data.
    nav[parts] = doc_path.as_posix()
    mkdocs_gen_files.set_edit_path(full_doc_path, path)

    # Save in-memory file.
    with mkdocs_gen_files.open(full_doc_path, "w") as writer:
        ident = ".".join(parts)
        writer.write(f"# {ident}\n\n")
        writer.write(f"::: {ident}")

    # Save to disk if requested.
    if temp_dir is not None:
        temp_path = temp_dir / doc_path
        temp_path.parent.mkdir(exist_ok=True, parents=True)
        with open(temp_path, "w") as writer:
            ident = ".".join(parts)
            writer.write(f"# {ident}\n\n")
            writer.write(f"::: {ident}")

# Generate navigation summary.
with mkdocs_gen_files.open("reference/SUMMARY.md", "w") as writer:
    writer.writelines(nav.build_literate_nav())
if temp_dir is not None:
    temp_path = temp_dir / "SUMMARY.md"
    with open(temp_path, "w") as writer:
        writer.writelines(nav.build_literate_nav())
