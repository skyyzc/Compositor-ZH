#!/usr/bin/env python3
import json, pathlib, subprocess
root = pathlib.Path(__file__).resolve().parents[1]
config = json.loads((root / 'upstream.json').read_text())
source = root / 'upstream'
if not source.exists():
    subprocess.run(['git', 'init', str(source)], check=True)
    subprocess.run(['git', '-C', str(source), 'remote', 'add', 'origin', config['repository']], check=True)
if subprocess.check_output(['git', '-C', str(source), 'remote', 'get-url', 'origin'], text=True).strip() != config['repository']:
    raise SystemExit('Unexpected upstream origin')
subprocess.run(['git', '-C', str(source), 'fetch', '--depth', '1', 'origin', config['commit']], check=True)
subprocess.run(['git', '-C', str(source), 'checkout', '--detach', config['commit']], check=True)
