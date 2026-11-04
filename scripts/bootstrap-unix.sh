#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

PROFILE="${AI_STANDARDS_PROFILE:-personal}"
ORG="${AI_STANDARDS_ORG:-}"
AGENTS="${AI_STANDARDS_AGENTS:-both}"

if ! command -v python3 >/dev/null 2>&1; then
    echo "ERROR: Python 3 is required."
    exit 1
fi

echo "AI Engineering Standards Bootstrap"
echo "Repository: $ROOT"
echo "Profile: $PROFILE"
echo "Organization: ${ORG:-none}"
echo "Agents: $AGENTS"

python3 "$ROOT/scripts/render-instructions.py" \
    --repo-root "$ROOT" \
    --profile "$PROFILE" \
    --org "$ORG" \
    --agents "$AGENTS"

echo ""
echo "Bootstrap complete."
echo "Claude instructions: ~/.claude/CLAUDE.md"
echo "Codex instructions:  ~/.codex/AGENTS.md"

