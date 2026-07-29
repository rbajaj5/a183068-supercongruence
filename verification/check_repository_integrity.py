"""Check repository navigation, Markdown fences, and protected documents."""

from __future__ import annotations

import hashlib
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROTECTED = {
    "BALA_VERSION.md": (
        "6ac0d1bdc83af028475a3a0663435385da68808a7fda282b6029089eb38a7862"
    ),
}
LINK_PATTERN = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")


def check_protected_files() -> int:
    checks = 0
    for relative, expected in PROTECTED.items():
        path = ROOT / relative
        actual = hashlib.sha256(path.read_bytes()).hexdigest()
        assert actual == expected, (
            f"{relative} changed: expected sha256 {expected}, found {actual}"
        )
        checks += 1
    return checks


def local_target(raw_target: str) -> str | None:
    target = raw_target.strip()
    if target.startswith("<") and target.endswith(">"):
        target = target[1:-1]
    if target.startswith(("http://", "https://", "mailto:", "#")):
        return None
    # LaTeX coefficient extraction such as ``[x^N](1+x+x^3)`` has the same
    # character shape as a Markdown link. Local repository links here name a
    # file or directory and therefore contain a path separator or extension.
    if "/" not in target and "\\" not in target and "." not in target:
        return None
    return target.split("#", 1)[0]


def check_markdown_links() -> int:
    checks = 0
    for markdown in sorted(ROOT.rglob("*.md")):
        if ".git" in markdown.parts or "tmp" in markdown.parts:
            continue
        text = markdown.read_text(encoding="utf-8")
        for match in LINK_PATTERN.finditer(text):
            relative = local_target(match.group(1))
            if not relative:
                continue
            destination = (markdown.parent / relative).resolve()
            assert destination.exists(), (
                f"broken local link in {markdown.relative_to(ROOT)}: "
                f"{match.group(1)}"
            )
            checks += 1
    return checks


def check_fences() -> int:
    checks = 0
    for markdown in sorted(ROOT.rglob("*.md")):
        if ".git" in markdown.parts or "tmp" in markdown.parts:
            continue
        text = markdown.read_text(encoding="utf-8")
        fence_count = sum(
            1 for line in text.splitlines() if line.lstrip().startswith("```")
        )
        assert fence_count % 2 == 0, (
            f"unbalanced Markdown fence in {markdown.relative_to(ROOT)}"
        )
        checks += 1
    return checks


def main() -> None:
    protected = check_protected_files()
    links = check_markdown_links()
    fences = check_fences()
    print(f"protected-file checks: {protected}")
    print(f"local-link checks: {links}")
    print(f"Markdown-fence checks: {fences}")
    print(f"all {protected + links + fences} repository integrity checks passed")


if __name__ == "__main__":
    main()
