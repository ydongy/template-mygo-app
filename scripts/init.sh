#!/usr/bin/env bash
# Usage: scripts/init.sh <Name> <domain> [--license mit|proprietary] [--owner <github-user>] [--repo <repository-name>]
set -euo pipefail
cd "$(dirname "$0")/.."
exec python3 scripts/init.py "$@"
