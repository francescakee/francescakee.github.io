#!/usr/bin/env python3
"""
Generates a YAML-style carousel/thumb listing from image files.

- 'carousel' = images in the current directory, sorted by date descending
- 'thumb'    = images in the ./thumbs/ subdirectory, sorted by date descending

Extensions are stripped from all filenames.

Usage:
    python generate_yaml.py                  # prints to stdout
    python generate_yaml.py -o output.yaml   # writes to a file
"""

import os
import sys
import argparse
from pathlib import Path

SUPPORTED_EXTENSIONS = {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp", ".tiff", ".tif"}


def get_images_sorted(directory: Path) -> list[str]:
    """Return image stems from a directory, sorted by modification date descending."""
    if not directory.is_dir():
        return []

    files = [
        f for f in directory.iterdir()
        if f.is_file() and f.suffix.lower() in SUPPORTED_EXTENSIONS
    ]
    files.sort(key=lambda f: f.stat().st_mtime, reverse=True)
    return [f.stem for f in files]


def build_yaml_block(label: str, names: list[str]) -> str:
    if not names:
        return f"{label}: []\n"
    lines = [f"{label}:"]
    for name in names:
        lines.append(f'  - "{name}"')
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate YAML carousel/thumb image listing.")
    parser.add_argument("-o", "--output", help="Write output to this file instead of stdout")
    parser.add_argument("directory", nargs="?", default=".", help="Source directory (default: current)")
    args = parser.parse_args()

    src = Path(args.directory).resolve()
    thumbs_dir = src / "thumb"

    carousel_names = get_images_sorted(src)
    thumb_names = get_images_sorted(thumbs_dir)

    if not carousel_names and not thumb_names:
        print("No supported images found.", file=sys.stderr)
        sys.exit(1)

    output = build_yaml_block("carousel", carousel_names)
    output += "\n\n"
    output += build_yaml_block("thumbs", thumb_names)
    output += "\n"

    if args.output:
        Path(args.output).write_text(output, encoding="utf-8")
        print(f"Written to '{args.output}'")
    else:
        print(output)


if __name__ == "__main__":
    main()
