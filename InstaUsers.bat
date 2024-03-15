@echo off
where python.exe > nul 2>&1
if %errorlevel% neq 0 (
    echo Python not found. Please make sure Python is installed.
    pause
) else (
    python "InstaInfo.py"
    pause
)