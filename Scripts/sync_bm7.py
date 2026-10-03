"""Manual BM7-only sync; AI, Crypto and other upstreams remain unchanged."""
import subprocess,sys
from pathlib import Path
if __name__=='__main__':
    subprocess.run([sys.executable,str(Path(__file__).with_name('sync_rules.py')),'--source','blackmatrix7/ios_rule_script'],check=True)
