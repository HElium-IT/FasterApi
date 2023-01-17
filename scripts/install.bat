@echo off

setlocal

set APP_FOLDER=%~dp0

set PYTHON_EXE=python3

set SCRIPT_NAME=fastapicli.py

set ALIAS=fastapicli

set ALIAS_CMD=%PYTHON_EXE% %APP_FOLDER%%SCRIPT_NAME% %*

doskey %ALIAS%=%ALIAS_CMD%

echo Alias %ALIAS% created.

endlocal

echo Press enter to continue
pause