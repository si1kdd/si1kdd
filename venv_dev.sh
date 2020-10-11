#!/usr/bin/env bash

"""
    This script create a virtualenv environment in a directotry called venv.
    And install optional dependencies into it.
"""

set -eu
set -o pipefail

echo "[*] Creating dev environment in ./venv ......"
echo ""

python3 -m venv ven
. venv/bin/activate
echo "[*] Created virtualenv environment in ./venv"

pip3 install -U pip setuptools
pip3 install -r requirements.txt
echo "[*] Installed all dependencies into the virtualenv"

echo ""
echo "[*] You can now activate the $(python3 --version) virtualenv with the command: \`. venv/bin/activate\`"
