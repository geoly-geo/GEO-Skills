#!/bin/bash
# Auto git commit and push script

REPO_DIR="/Users/gao/.openclaw/workspace-clawhub-bot"
cd "$REPO_DIR" || exit 1

# Check if there are changes
if git diff --quiet && git diff --cached --quiet; then
    # No changes
    exit 0
fi

# Add all changes
git add -A

# Create commit message with timestamp
COMMIT_MSG="Auto commit: $(date '+%Y-%m-%d %H:%M:%S')

Changes:
$(git status --short)"

# Commit
git commit -m "$COMMIT_MSG"

# Push to origin
git push origin main

echo "Committed and pushed at $(date)"
