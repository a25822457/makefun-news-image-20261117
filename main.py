#!/usr/bin/env python3
"""Copy the finished front page to /output/entry.png.

Standard library only, no network. The image is rendered at build time
(see render.py) and shipped in this repository as entry.png; this program
just copies it to the output path make.fun expects, deterministically.
"""
import os
import shutil
import sys
from pathlib import Path


def main(argv):
    here = Path(__file__).resolve().parent
    src = here / "entry.png"
    if len(argv) > 1:
        dest = Path(argv[1])
    elif os.environ.get("MAKEFUN_OUTPUT_DIR"):
        dest = Path(os.environ["MAKEFUN_OUTPUT_DIR"]) / "entry.png"
    else:
        dest = Path("/output/entry.png")
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(src, dest)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
