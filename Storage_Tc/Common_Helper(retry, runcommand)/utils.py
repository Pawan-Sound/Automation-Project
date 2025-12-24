# utils.py
import subprocess
import shlex
import time
from typing import Tuple

def run_cmd(cmd: str, timeout: int = 10) -> Tuple[int, str, str]:
    """Run shell command; return (returncode, stdout, stderr)."""
    proc = subprocess.run(shlex.split(cmd), capture_output=True, text=True, timeout=timeout)
    return proc.returncode, proc.stdout.strip(), proc.stderr.strip()

def retry(func, retries=3, delay=2, *args, **kwargs):
    """Simple retry helper; returns func(*args, **kwargs) or raises last exception."""
    last_exc = None
    for i in range(retries):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            last_exc = e
            time.sleep(delay)
    raise last_exc
    #break
