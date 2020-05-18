#!/bin/bash
echo "Starting Rest Services..."
cd "$(dirname "${BASH_SOURCE[0]}")"
cd venv/bin
. activate
cd ../../
python -m http.server --cgi 8000
echo "Local PurePy Rest stopped."
echo ""

