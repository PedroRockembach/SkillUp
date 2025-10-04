Quick run instructions

If PowerShell refuses to run `Activate.ps1` due to execution policy, use one of the helpers below which run the venv python directly (no activation required).

From PowerShell (preferred):

1. Ensure you are in the project root:
   cd 'C:\Users\rocke\OneDrive\Documentos\GitHub\SkillUp\backend'

2. Create a virtualenv (if you haven't):
   python -m venv .venv

3. Run the PowerShell helper (this launches a new process and uses the venv python):
   powershell -ExecutionPolicy Bypass -File .\run.ps1

Or run the batch helper (works from cmd or PowerShell):

   .\run.bat

Or run uvicorn directly without activating the venv (single command):

   .\.venv\Scripts\python.exe -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8000

Notes
- The scripts install requirements from `requirements.txt` if present.
- We use the qualified module path `app.main:app` to avoid importing the wrong `main.py` (you had a `database/main.py` too).
- If you prefer to allow PowerShell scripts permanently, you can change execution policy (requires admin):
  Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
  But I recommend the helper scripts above for minimal, safe changes.