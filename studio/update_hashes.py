#!/usr/bin/env python3
"""Refresh ATTRIBUTION.toml hashes for files we changed (after `studio/rebrand.py` or a merge).

    python3 studio/update_hashes.py    # rewrites the sha256 of every entry `cargo xtask assets` flags
"""
import hashlib
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
out = subprocess.run(['cargo', 'xtask', 'assets'], cwd=ROOT, capture_output=True, text=True)
paths = sorted(set(re.findall(r'✗ (\S+): SHA-256 does not match', out.stdout + out.stderr)))
toml = ROOT / 'ATTRIBUTION.toml'
t = toml.read_text(encoding='utf-8')
for p in paths:
    h = hashlib.sha256((ROOT / p).read_bytes()).hexdigest()
    t, n = re.subn(r'(path = "%s"\n(?:(?!\[\[asset\]\]).)*?sha256 = ")[0-9a-f]+' % re.escape(p), r'\g<1>' + h, t, flags=re.S)
    print(('updated ' if n else 'no entry for ') + p)
toml.write_text(t, encoding='utf-8')
