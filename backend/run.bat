@echo off
REM Helper batch file that uses the venv python directly (no PowerShell activation required)
if not exist ".venv\Scripts\python.exe" (
  echo Virtualenv not found. Create with: python -m venv .venv
  exit /b 1
)
.venv\Scripts\python.exe -m pip install --upgrade pip
if exist requirements.txt (
  .venv\Scripts\python.exe -m pip install -r requirements.txt
)
.venv\Scripts\python.exe -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
