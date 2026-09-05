#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

import yaml

PANDOC_VERSION = "3.1.11.1"


def pandoc_version() -> str:
    result = subprocess.run(["pandoc", "--version"], text=True, capture_output=True)
    if result.returncode != 0:
        raise RuntimeError("Pandoc finns inte i PATH.")
    match = re.search(r"pandoc\s+([^\s]+)", result.stdout.splitlines()[0])
    return match.group(1) if match else "unknown"


def run(command: list[str], cwd: Path) -> None:
    print("+", " ".join(command))
    subprocess.run(command, cwd=cwd, check=True)


def latex_escape(text: str) -> str:
    replacements = {
        "\\": r"\textbackslash{}", "&": r"\&", "%": r"\%", "$": r"\$",
        "#": r"\#", "_": r"\_", "{": r"\{", "}": r"\}",
        "~": r"\textasciitilde{}", "^": r"\textasciicircum{}",
    }
    return "".join(replacements.get(char, char) for char in text)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".")
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--formats", default="epub,pdf")
    parser.add_argument("--name", default="")
    parser.add_argument("--allow-pandoc-version-mismatch", action="store_true")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    output_dir = Path(args.output_dir).resolve()
    run([sys.executable, "scripts/validate_project.py", "."], root)

    version = pandoc_version()
    if version != PANDOC_VERSION and not args.allow_pandoc_version_mismatch:
        print(f"ERROR: Pandoc {PANDOC_VERSION} krävs; hittade {version}.", file=sys.stderr)
        return 2

    metadata_path = root / "book.yaml"
    metadata = yaml.safe_load(metadata_path.read_text(encoding="utf-8")) or {}
    chapters = [root / rel for rel in metadata["chapters"]]
    output_dir.mkdir(parents=True, exist_ok=True)
    base_name = args.name or metadata.get("project_slug", "book")
    formats = {part.strip().lower() for part in args.formats.split(",") if part.strip()}
    if not formats or not formats <= {"epub", "pdf"}:
        print("ERROR: --formats måste vara epub och/eller pdf.", file=sys.stderr)
        return 2

    resource_path = f"{root}:{root / 'chapters'}"
    chapter_filter = root / "publishing/chapter-headings.lua"
    common = [
        "--metadata-file", str(metadata_path),
        "--resource-path", resource_path,
        "--lua-filter", str(chapter_filter),
        "--toc-depth=1",
    ]

    if "epub" in formats:
        epub = output_dir / f"{base_name}.epub"
        run([
            "pandoc", *map(str, chapters),
            "--from=markdown", "--to=epub3",
            "--output", str(epub),
            *common,
            "--css", str(root / "publishing/epub.css"),
            "--epub-cover-image", str(root / metadata["cover_image"]),
        ], root)
        print(f"OK: EPUB skapad: {epub}")

    if "pdf" in formats:
        if shutil.which("xelatex") is None:
            print("ERROR: xelatex krävs för PDF-bygget.", file=sys.stderr)
            return 2

        pdf = output_dir / f"{base_name}.pdf"
        with tempfile.TemporaryDirectory(prefix="ai-strategi-pdf-") as tmp:
            frontmatter = Path(tmp) / "frontmatter.tex"
            cover = (root / metadata["cover_image"]).as_posix()
            title = latex_escape(str(metadata.get("title", "")))
            subtitle = latex_escape(str(metadata.get("subtitle", "")))
            author = latex_escape(str(metadata.get("author", "")))
            frontmatter.write_text(
                "\\thispagestyle{empty}\n"
                f"\\noindent\\includegraphics[width=\\paperwidth,height=\\paperheight]{{{cover}}}\n"
                # Changing geometry here flushes the cover page and then applies
                # the normal book margins. Doing it before the cover would create
                # an empty first page.
                "\\newgeometry{margin=22mm}\n"
                "\\thispagestyle{empty}\n"
                "\\vspace*{0.18\\textheight}\n"
                "\\begin{center}\n"
                f"{{\\Huge\\bfseries {title}}}\\par\n"
                f"\\vspace{{1em}}{{\\Large {subtitle}}}\\par\n"
                "\\vfill\n"
                f"{{\\Large {author}}}\\par\n"
                "\\end{center}\\clearpage\n",
                encoding="utf-8",
            )

            run([
                "pandoc", *map(str, chapters),
                "--from=markdown", "--to=pdf",
                "--pdf-engine=xelatex", "--output", str(pdf),
                *common,
                "--toc",
                "--metadata", "title=",
                "--include-in-header", str(root / "publishing/pdf-header.tex"),
                "--include-before-body", str(frontmatter),
                "-V", "papersize=a4",
                "-V", "geometry:margin=22mm",
                "-V", "fontsize=11pt",
                "-V", "mainfont=TeX Gyre Pagella",
                "-V", "sansfont=TeX Gyre Heros",
                "-V", "colorlinks=true",
                "-V", "linkcolor=black",
                "-V", "urlcolor=blue",
            ], root)
        print(f"OK: PDF skapad: {pdf}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
