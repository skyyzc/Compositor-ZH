#!/usr/bin/env python3
"""Explicitly check upstream, rebuild localization, and report new translation work."""
import pathlib, subprocess, sys
root = pathlib.Path(__file__).resolve().parents[1]
# Updating is explicit. No background installation or replacement of a running app.
subprocess.run(['git', '-C', str(root / 'upstream'), 'fetch', '--depth', '1', 'origin', 'main'], check=True)
subprocess.run(['git', '-C', str(root / 'upstream'), 'checkout', '--detach', 'FETCH_HEAD'], check=True)
subprocess.run([sys.executable, str(root / 'scripts/prepare.py'), '--require-complete'], check=True)
print('静态候选翻译检查通过；动态界面、构建和运行仍需验证。')
