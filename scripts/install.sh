#!/bin/bash

APP_FOLDER="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

PYTHON_EXE=python3

SCRIPT_NAME=main.py

ALIAS=fastapicli

ALIAS_CMD="$PYTHON_EXE $APP_FOLDER/$SCRIPT_NAME"

echo "alias $ALIAS='$ALIAS_CMD'" >> ~/.bashrc

source ~/.bashrc

echo "Alias $ALIAS created"

read -p "Press enter to continue"