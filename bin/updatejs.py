"""Check code."""

import argparse
from pathlib import Path

import utils


def main():
    """Main driver."""

    args = parse_args()
    codedir = utils.select_code_directory(args)
    if args.dev:
        utils.update_plotlyjs_dev(codedir)
    else:
        version = utils.plotly_js_version()
        print(version)
        utils.update_plotlyjs(version, codedir)


def parse_args():
    """Parse command-line arguments."""

    parser = argparse.ArgumentParser()
    parser.add_argument("--dev", action="store_true", help="development version")
    parser.add_argument("--codedir", type=Path, help="code directory")
    return parser.parse_args()


if __name__ == "__main__":
    main()
