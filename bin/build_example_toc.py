from collections import defaultdict
from pathlib import Path
import sys
import yaml


SKIPS = {"getting-started.md"}


def main():
    """Main driver."""
    sources = [Path(a) for a in sys.argv[1:]]
    sources = [src for src in sources if str(src.name) not in SKIPS]

    sections = defaultdict(list)
    for src in sources:
        try:
            content = src.read_text()
            header = content.split("---")[1].strip()
            data = yaml.safe_load(header)
            data = data["jupyter"]["plotly"]
            display = data["display_as"]
            order = float(data["order"])
            sections[display].append((order, data, src.name))
        except Exception as exc:
            print(f"failed to load from {src}: {exc}", file=sys.stderr)

    for key, values in sorted(sections.items()):
        values.sort(key=lambda x: float(x[0]))
        print(f"- {key}")
        for order, data, src in values:
            print(f'  - {src}: "{data["name"]}"')


if __name__ == "__main__":
    main()
