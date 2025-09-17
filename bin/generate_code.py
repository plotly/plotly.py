"""Generate code."""

import argparse
from pathlib import Path

import utils


def main():
    """Main driver."""

    args = parse_args()
    codedir = utils.select_code_directory(args)
    utils.perform_codegen(codedir, noformat=args.noformat, schema=args.schema)


def parse_args():
    """Parse command-line arguments."""

    parser = argparse.ArgumentParser()
    parser.add_argument("--codedir", type=Path, help="code directory")
    parser.add_argument("--noformat", action="store_true", help="prevent reformatting")
    parser.add_argument(
        "--schema",
        type=Path,
        default=utils.PLOT_SCHEMA,
        help=f"schema file (default {utils.PLOT_SCHEMA})",
    )
    return parser.parse_args()


if __name__ == "__main__":
    main()
