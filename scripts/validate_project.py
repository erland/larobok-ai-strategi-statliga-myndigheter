#!/usr/bin/env python3
from __future__ import annotations

import sys
from pathlib import Path

import yaml


def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    metadata_path = root / "book.yaml"
    if not metadata_path.exists():
        print("ERROR: book.yaml saknas.", file=sys.stderr)
        return 2

    metadata = yaml.safe_load(metadata_path.read_text(encoding="utf-8")) or {}
    required = ["title", "author", "language", "project_slug", "cover_image", "chapters"]
    missing = [key for key in required if not metadata.get(key)]
    if missing:
        print("ERROR: metadata saknar: " + ", ".join(missing), file=sys.stderr)
        return 2

    cover = root / metadata["cover_image"]
    if not cover.exists():
        print(f"ERROR: omslagsbild saknas: {metadata['cover_image']}", file=sys.stderr)
        return 2

    chapters = metadata["chapters"]
    if not isinstance(chapters, list) or not chapters:
        print("ERROR: chapters måste vara en icke-tom lista.", file=sys.stderr)
        return 2

    for rel in chapters:
        path = root / rel
        if not path.exists():
            print(f"ERROR: kapitel saknas: {rel}", file=sys.stderr)
            return 2
        text = path.read_text(encoding="utf-8")
        if not any(line.startswith("# ") for line in text.splitlines()):
            print(f"ERROR: kapitel saknar H1-rubrik: {rel}", file=sys.stderr)
            return 2

    if chapters[0] != "chapters/00-inledning.md":
        print("ERROR: första kapitlet ska vara chapters/00-inledning.md.", file=sys.stderr)
        return 2

    print(f"OK: {metadata['title']} – {len(chapters)} manusfiler och omslag verifierade.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
