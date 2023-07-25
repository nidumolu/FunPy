import subprocess
from pathlib import Path
VENV_NAME = '.venv'
REQUIREMENTS = 'requirements.txt'
process = subprocess.run(['which', 'python3'], capture_output=True, text=True)
if process.returncode != 0:
    raise OSError('Sorry python3 is not installed')
python_process = process.stdout.strip()
print(f'Python found in: {python_process}')