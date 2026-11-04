#!/usr/bin/env python3
"""Render shared engineering standards into Claude and Codex instructions."""

import argparse
import os
import re
import shutil
import sys
from pathlib import Path

BEGIN = "<!-- BEGIN AI-ENGINEERING-STANDARDS MANAGED -->"
END = "<!-- END AI-ENGINEERING-STANDARDS MANAGED -->"

def read_sections(repo, files):
    sections = []
    for relative in files:
        path = repo / relative
        if not path.is_file():
            raise FileNotFoundError(f"Required standards file missing: {path}")
        sections.append(
            f"\n\n<!-- Source: {relative} -->\n\n{path.read_text(encoding='utf-8').strip()}"
        )
    return "\n".join(sections).strip()

def update_file(target, managed_content):
    target.parent.mkdir(parents=True, exist_ok=True)

    if target.is_symlink():
        raise RuntimeError(
            f"Refusing to modify symlink: {target}. "
            "Resolve it explicitly before bootstrapping."
        )

    existing = target.read_text(encoding="utf-8") if target.exists() else ""

    if (BEGIN in existing) != (END in existing):
        raise RuntimeError(f"Unmatched managed markers in {target}")

    block = f"{BEGIN}\n\n{managed_content}\n\n{END}"

    if BEGIN in existing:
        start = existing.index(BEGIN)
        finish = existing.index(END) + len(END)
        updated = existing[:start] + block + existing[finish:]
    else:
        if existing.strip():
            backup = target.with_name(target.name + ".pre-ai-standards.bak")
            if not backup.exists():
                shutil.copy2(target, backup)
        updated = existing.rstrip() + "\n\n" + block + "\n"

    if updated != existing:
        temp = target.with_name(target.name + ".tmp")
        temp.write_text(updated, encoding="utf-8")
        os.replace(temp, target)
        print(f"Updated: {target}")
    else:
        print(f"Already current: {target}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", required=True)
    parser.add_argument(
        "--profile",
        choices=["personal", "organization", "combined"],
        default="personal",
    )
    parser.add_argument("--org", default="")
    parser.add_argument(
        "--agents", choices=["both", "claude", "codex"], default="both"
    )
    args = parser.parse_args()

    repo = Path(args.repo_root).resolve()

    if not (repo / "standards/common").is_dir():
        sys.exit("Not a valid standards repository: standards/common missing")

    if args.profile in ("organization", "combined") and not args.org:
        sys.exit("--org is required for organization or combined profile")

    if args.org and not re.fullmatch(r"[a-zA-Z0-9_-]+", args.org):
        sys.exit("Invalid organization profile name")

    common = sorted(
        str(p.relative_to(repo))
        for p in (repo / "standards/common").glob("*.md")
    )

    if not common:
        sys.exit("No common standards found")

    profile_files = []

    if args.profile in ("personal", "combined"):
        profile_files.append("standards/personal/INSTRUCTIONS.md")

    if args.profile in ("organization", "combined"):
        profile_files.append(
            f"standards/organizations/{args.org}/INSTRUCTIONS.md"
        )

    home = Path.home()
    claude_home = Path(
        os.environ.get("CLAUDE_CONFIG_DIR", str(home / ".claude"))
    )
    codex_home = Path(os.environ.get("CODEX_HOME", str(home / ".codex")))

    targets = []

    if args.agents in ("both", "claude"):
        files = common + profile_files + ["agents/claude/INSTRUCTIONS.md"]
        content = read_sections(repo, files)
        targets.append((claude_home / "CLAUDE.md", content))

    if args.agents in ("both", "codex"):
        files = common + profile_files + ["agents/codex/INSTRUCTIONS.md"]
        content = read_sections(repo, files)
        targets.append((codex_home / "AGENTS.md", content))

    for target, content in targets:
        update_file(target, content)

    print("Engineering standards bootstrap completed.")

if __name__ == "__main__":
    main()

