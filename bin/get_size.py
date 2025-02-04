"""Calculate total size and total number of files of package."""

from pathlib import Path
import sys


def main():
    """Main driver."""
    assert 2 <= len(sys.argv) <= 3, "Usage: get_size.py src_dir [build_dir]"

    src_files, src_bytes = get_size(sys.argv[1])
    print(f"src,files,{src_files}")
    print(f"src,bytes,{src_bytes}")

    if len(sys.argv) == 3:
        build_files, build_bytes = get_size(sys.argv[2])
        print(f"build,files,{build_files}")
        print(f"build,bytes,{build_bytes}")


def get_size(root_dir):
    """Count files and size in bytes."""
    num_files, num_bytes = 0, 0
    for f in Path(root_dir).glob("**/*.*"):
        if "__pycache__" not in str(f):
            num_files += 1
            num_bytes += f.stat().st_size
    return num_files, num_bytes


if __name__ == "__main__":
    main()
