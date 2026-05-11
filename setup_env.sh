#!/usr/bin/env bash

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

PROJECT_NAME="Rule-Based Cognitive Architecture"
VENV_DIR=".venv"
PYTHON_VERSION="python3"

echo -e "${BLUE}========================================${NC}"
echo -e "${BLUE}Setting up ${PROJECT_NAME}${NC}"
echo -e "${BLUE}========================================${NC}"
echo

echo -e "${YELLOW}[1/5] Checking Python installation...${NC}"
if ! command -v "$PYTHON_VERSION" >/dev/null 2>&1; then
    echo -e "${RED}Error: Python 3 is not installed.${NC}"
    exit 1
fi
echo -e "${GREEN}✓ Found: $($PYTHON_VERSION --version)${NC}"
echo

echo -e "${YELLOW}[2/5] Checking venv support...${NC}"
if ! "$PYTHON_VERSION" -m venv --help >/dev/null 2>&1; then
    echo -e "${RED}Error: python3-venv is not available.${NC}"
    echo -e "${RED}Install it with your OS package manager and run this script again.${NC}"
    exit 1
fi
echo -e "${GREEN}✓ venv module is available${NC}"
echo

echo -e "${YELLOW}[3/5] Creating or repairing virtual environment...${NC}"
if [ ! -d "$VENV_DIR" ]; then
    "$PYTHON_VERSION" -m venv "$VENV_DIR"
    echo -e "${GREEN}✓ Virtual environment created at ${VENV_DIR}${NC}"
else
    echo -e "${GREEN}✓ Virtual environment already exists${NC}"
fi

if ! "$VENV_DIR/bin/python" -m pip --version >/dev/null 2>&1; then
    echo -e "${YELLOW}Existing virtual environment has a broken pip install. Recreating ${VENV_DIR}...${NC}"
    rm -rf "$VENV_DIR"
    "$PYTHON_VERSION" -m venv "$VENV_DIR"
    echo -e "${GREEN}✓ Virtual environment recreated${NC}"
fi
echo

echo -e "${YELLOW}[4/5] Bootstrapping packaging tools...${NC}"
"$VENV_DIR/bin/python" -m ensurepip --upgrade >/dev/null 2>&1 || true
"$VENV_DIR/bin/python" -m pip install --upgrade pip setuptools wheel
echo -e "${GREEN}✓ Packaging tools upgraded${NC}"
echo

echo -e "${YELLOW}[5/5] Installing project dependencies...${NC}"
if [ ! -f "requirements.txt" ]; then
    echo -e "${RED}Error: requirements.txt not found.${NC}"
    exit 1
fi
"$VENV_DIR/bin/python" -m pip install -r requirements.txt
echo -e "${GREEN}✓ Dependencies installed${NC}"
echo

echo -e "${BLUE}========================================${NC}"
echo -e "${GREEN}Setup completed successfully${NC}"
echo -e "${BLUE}========================================${NC}"
echo
echo -e "${YELLOW}Activate the environment with:${NC}"
echo -e "${BLUE}source ${VENV_DIR}/bin/activate${NC}"
