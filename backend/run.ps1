# Helper PowerShell runner that avoids Activation script execution policy issues
# It uses the virtualenv's python executable directly so you don't need to run Activate.ps1.

$PSScriptRoot = Split-Path -Parent $MyInvocation.MyCommand.Definition
$venvPython = Join-Path $PSScriptRoot '.venv\Scripts\python.exe'

if (-Not (Test-Path $venvPython)) {
    Write-Host "Virtualenv not found at .venv. Create it with: python -m venv .venv" -ForegroundColor Yellow
    exit 1
}

Write-Host "Using venv python: $venvPython"

# Upgrade pip and install requirements if present
& $venvPython -m pip install --upgrade pip
if (Test-Path (Join-Path $PSScriptRoot 'requirements.txt')) {
    & $venvPython -m pip install -r (Join-Path $PSScriptRoot 'requirements.txt')
}

# Run uvicorn using the venv python (qualified module path avoids main.py collisions)
& $venvPython -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
