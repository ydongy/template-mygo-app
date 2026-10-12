#!/usr/bin/env bash
# Usage: scripts/init.sh <Name> <domain> [--license mit|proprietary] [--owner <github-user>] [--repo <repository-name>]
# (installs README.md and README.zh-CN.md of the chosen license skeleton; see .template/README.md)
set -euo pipefail
cd "$(dirname "$0")/.."
exec python3 scripts/init.py "$@"
