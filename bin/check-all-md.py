from pathlib import Path
import os
import sys
from run_markdown import _parse_md

TMP_FILE = "tmp.py"

for filename in sys.argv[1:]:
    content = Path(filename).read_text()
    blocks = _parse_md(content)
    for i, block in enumerate(blocks):
        Path(TMP_FILE).write_text(block["code"].strip())
        sys.stdout.write(f"\n{'=' * 40}\n{filename}: {i}\n")
        sys.stdout.flush()
        sys.stdout.write(f"{'-' * 40}\n")
        sys.stdout.flush()
        os.system(f"python {TMP_FILE} > /dev/null")
