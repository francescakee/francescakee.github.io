#!/usr/bin/env python3
"""
Batch image resizer — creates ~175x175 thumbnails in a 'thumbs' subfolder.
Thumbnails are named with '-thumb' appended before the file extension.

Usage:
    python resize_thumbs.py                      # resizes all images in current dir
    python resize_thumbs.py /path/to/images      # resizes all images in given dir
    python resize_thumbs.py img1.jpg img2.png    # resizes specific files
"""

import sys
import os
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    print("Pillow is required. Install it with:  pip install Pillow")
    sys.exit(1)

THUMB_SIZE = (175, 175)
SUPPORTED_EXTENSIONS = {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp", ".tiff", ".tif"}


def make_thumb(src: Path, out_dir: Path) -> None:
    """Resize a single image and save it to out_dir with a -thumb suffix."""
    #dest_name = src.stem + "-thumb" + src.suffix
    dest_name = src.stem + src.suffix
    dest = out_dir / dest_name

    with Image.open(src) as img:
        img.thumbnail(THUMB_SIZE, Image.LANCZOS)
        # Preserve EXIF data for JPEGs where possible
        save_kwargs = {}
        if src.suffix.lower() in {".jpg", ".jpeg"}:
            save_kwargs["quality"] = 90
            save_kwargs["optimize"] = True
        img.save(dest, **save_kwargs)

    print(f"  ✓  {src.name}  →  {dest.relative_to(src.parent.parent if out_dir.parent == src.parent else out_dir.parent)}")


def collect_images(targets: list[str]) -> list[Path]:
    """Return a flat list of image paths from the given files/directories."""
    images = []
    for t in targets:
        p = Path(t)
        if p.is_dir():
            for ext in SUPPORTED_EXTENSIONS:
                images.extend(p.glob(f"*{ext}"))
                images.extend(p.glob(f"*{ext.upper()}"))
        elif p.is_file() and p.suffix.lower() in SUPPORTED_EXTENSIONS:
            images.append(p)
        else:
            print(f"  ⚠  Skipping '{t}' (not a supported image or directory)")
    return sorted(set(images))


def main() -> None:
    targets = sys.argv[1:] if len(sys.argv) > 1 else ["."]
    images = collect_images(targets)

    if not images:
        print("No supported images found.")
        return

    # Group by source directory so each dir gets its own 'thumb' subfolder
    by_dir: dict[Path, list[Path]] = {}
    for img in images:
        by_dir.setdefault(img.parent, []).append(img)

    total, failed = 0, 0
    for src_dir, files in by_dir.items():
        out_dir = src_dir / "thumb"
        out_dir.mkdir(exist_ok=True)
        print(f"\nProcessing {len(files)} image(s) in '{src_dir}' → '{out_dir}'")

        for f in files:
            try:
                make_thumb(f, out_dir)
                total += 1
            except Exception as e:
                print(f"  ✗  {f.name}: {e}")
                failed += 1

    print(f"\nDone — {total} thumbnail(s) created" + (f", {failed} failed" if failed else "") + ".")


if __name__ == "__main__":
    main()
