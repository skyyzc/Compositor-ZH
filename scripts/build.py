#!/usr/bin/env python3
"""Build a reviewable local preview; does not install or replace any app."""
import pathlib, subprocess, sys
root = pathlib.Path(__file__).resolve().parents[1]
check = subprocess.run(['xcodebuild', '-version'], capture_output=True, text=True)
if check.returncode:
    sys.exit('BLOCKED：需要完整 Xcode。目前只有 Command Line Tools；请安装并首次打开 Xcode 完成组件安装。')
subprocess.run([sys.executable, str(root / 'scripts/prepare.py')], check=True)
subprocess.run(['xcodebuild', '-project', str(root / 'build-source/Compositor.xcodeproj'), '-scheme', 'Compositor', '-configuration', 'Debug', '-destination', 'platform=macOS', '-derivedDataPath', str(root / 'build'), 'CODE_SIGNING_ALLOWED=NO', 'build'], check=True)
app = root / 'build/Build/Products/Debug/Compositor 中文.app'
subprocess.run(['codesign', '--force', '--deep', '--sign', '-', str(app)], check=True)
subprocess.run(['codesign', '--verify', '--deep', '--strict', str(app)], check=True)
print(f'IMPLEMENTED_NOT_VERIFIED：预览程序已构建，仍需启动与功能验收：{app}')
