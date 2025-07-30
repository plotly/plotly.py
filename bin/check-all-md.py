from pathlib import Path
import os
import re
import sys

PAT = re.compile(r"^```python\n(.+?)\n```", re.MULTILINE | re.DOTALL)
TMP_FILE = "tmp.py"

for filename in sys.argv[1:]:
    content = Path(filename).read_text()
    blocks = PAT.findall(content)
    for i, b in enumerate(blocks):
        Path(TMP_FILE).write_text(b.strip())
        sys.stdout.write(f"\n{'=' * 40}\n{filename}: {i}\n")
        sys.stdout.flush()
        sys.stdout.write(f"{'-' * 40}\n")
        sys.stdout.flush()
        os.system(f"python {TMP_FILE} > /dev/null")
