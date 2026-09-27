"""`python -m fiuto_design`: writes the generated files; `--check` only verifies them."""

import argparse
import sys
from pathlib import Path

from fiuto_design import css, dart, typescript
from fiuto_design.tokens import load

ROOT = Path(__file__).resolve().parents[2]
SOURCE = Path("tokens/tokens.json")
LOGOS = Path("assets/logos")
# A Flutter package can only ship files inside its folder: the logos are copied there.
FLUTTER_LOGOS = Path("flutter/assets/logos")
OUTPUTS = {
    Path("web/tokens.css"): css.render,
    Path("web/tokens.ts"): typescript.render,
    Path("flutter/lib/fiuto_design.dart"): dart.render,
}


def generated(root: Path) -> dict[Path, str]:
    tokens = load(root / SOURCE)
    files = {path: render(tokens) for path, render in OUTPUTS.items()}
    for logo in sorted((root / LOGOS).glob("*.svg")):
        files[FLUTTER_LOGOS / logo.name] = logo.read_text(encoding="utf-8")
    return files


def main(argv: list[str] | None = None, root: Path = ROOT) -> int:
    parser = argparse.ArgumentParser(
        prog="python -m fiuto_design", description="Generates the token files."
    )
    parser.add_argument("--check", action="store_true", help="fail if a file is out of date")
    args = parser.parse_args(argv)
    stale = []
    for path, content in generated(root).items():
        target = root / path
        current = target.read_text(encoding="utf-8") if target.exists() else None
        if current == content:
            continue
        if args.check:
            stale.append(str(path))
        else:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(content, encoding="utf-8")
            print(f"written {path}")
    if stale:
        print(
            "out of date, run `python -m fiuto_design`: " + ", ".join(stale),
            file=sys.stderr,
        )
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
