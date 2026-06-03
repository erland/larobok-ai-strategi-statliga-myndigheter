#!/usr/bin/env python3
from pathlib import Path
import subprocess
import sys
import re
import yaml

ROOT = Path(__file__).resolve().parents[1]
META_PATHS = [ROOT / "docs" / "export-metadata.yaml", ROOT / "book.yaml"]

def read_metadata():
    for path in META_PATHS:
        if path.exists():
            with path.open("r", encoding="utf-8") as f:
                return yaml.safe_load(f), path
    raise SystemExit("Saknar docs/export-metadata.yaml eller book.yaml.")

def validate_metadata(meta):
    required = ["title", "author", "language", "identifier", "date", "version", "chapters"]
    missing = [k for k in required if not meta.get(k)]
    if missing:
        raise SystemExit("Metadata saknar obligatoriska fält: " + ", ".join(missing))

def count_table_cells(line):
    stripped = line.strip()
    if not stripped.startswith("|"):
        return None
    return len([p for p in stripped.strip("|").split("|")])

def validate_markdown(chapter_paths):
    errors = []
    for rel in chapter_paths:
        path = ROOT / rel
        if not path.exists():
            errors.append(f"Saknar kapitel: {rel}")
            continue
        text = path.read_text(encoding="utf-8")
        if re.search(r"^#{4,}\s", text, re.MULTILINE):
            errors.append(f"{rel}: innehåller H4 eller djupare rubriker.")
        if text.count("```") % 2 != 0:
            errors.append(f"{rel}: ojämnt antal kodblocksmarkörer.")
        lines = text.splitlines()
        for i, line in enumerate(lines):
            if line.strip().startswith("|"):
                if i + 1 < len(lines) and re.match(r"^\s*\|?\s*:?-{3,}:?\s*(\|\s*:?-{3,}:?\s*)+\|?\s*$", lines[i + 1]):
                    expected = count_table_cells(line)
                    j = i + 2
                    while j < len(lines) and lines[j].strip().startswith("|"):
                        if count_table_cells(lines[j]) != expected:
                            errors.append(f"{rel}: tabellrad {j+1} har fel antal celler.")
                        j += 1
    if errors:
        raise SystemExit("Markdownvalidering misslyckades:\n- " + "\n- ".join(errors))

def build_combined(chapters):
    build_dir = ROOT / "build"
    build_dir.mkdir(exist_ok=True)
    out = build_dir / "book.md"
    parts = []
    for rel in chapters:
        parts.append((ROOT / rel).read_text(encoding="utf-8").strip() + "\n")
    out.write_text("\n\n".join(parts), encoding="utf-8")
    return out

def run_pandoc(meta, combined, target):
    exports = ROOT / "exports"
    exports.mkdir(exist_ok=True)
    title = meta["title"]
    author = meta["author"]
    lang = "sv-SE" if meta.get("language") == "sv" else meta.get("language")
    slug = meta.get("project_slug", "book")

    if target in ("epub", "all"):
        cmd = [
            "pandoc", str(combined),
            "--from=gfm",
            "--to=epub3",
            "--metadata", f"title={title}",
            "--metadata", f"author={author}",
            "--metadata", f"lang={lang}",
            "--css=styles/epub.css",
            "--output", str(exports / f"{slug}.epub"),
        ]
        subprocess.run(cmd, cwd=ROOT, check=True)

    if target in ("pdf", "all"):
        cmd = [
            "pandoc", str(combined),
            "--from=gfm",
            "--pdf-engine=xelatex",
            "--toc",
            "--toc-depth=3",
            "--metadata", f"title={title}",
            "--metadata", f"author={author}",
            "--metadata", f"lang={lang}",
            "--output", str(exports / f"{slug}.pdf"),
        ]
        subprocess.run(cmd, cwd=ROOT, check=True)

def main():
    target = sys.argv[1] if len(sys.argv) > 1 else "all"
    meta, meta_path = read_metadata()
    validate_metadata(meta)
    chapters = meta["chapters"]
    validate_markdown(chapters)
    combined = build_combined(chapters)

    try:
        run_pandoc(meta, combined, target)
    except FileNotFoundError:
        raise SystemExit("Pandoc saknas. Installera Pandoc lokalt och kör scripts/export-book.sh igen.")
    except subprocess.CalledProcessError as e:
        raise SystemExit(f"Export misslyckades. Kontrollera att Pandoc och vald PDF-engine finns installerade. Felkod: {e.returncode}")

    print("Export klar. Se exports/.")

if __name__ == "__main__":
    main()
