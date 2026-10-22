#!/usr/bin/env python3
"""Publish an existing successful build on GitHub; never install or launch the app."""
import hashlib, json, os, pathlib, plistlib, re, shutil, subprocess
root = pathlib.Path(__file__).resolve().parents[1]
repo = os.environ['GITHUB_REPOSITORY']
run = os.environ['BUILD_RUN']
tag = os.environ['RELEASE_TAG']
if repo != 'skyyzc/Compositor-ZH' or not run.isdigit() or not re.fullmatch(r'v\d+\.\d+\.\d+-zh\.preview\.\d+', tag):
    raise SystemExit('Unexpected publication inputs')
def command(*args):
    subprocess.run(args, check=True)
metadata = json.loads(subprocess.check_output(['gh', 'api', f'repos/{repo}/actions/runs/{run}'], text=True))
if metadata['conclusion'] != 'success' or metadata['name'] != 'Chinese preview' or metadata['head_repository']['full_name'] != repo:
    raise SystemExit('A successful preview build from this repository is required')
source = root / 'dist/publish-input'
source.mkdir(parents=True, exist_ok=True)
command('gh', 'run', 'download', run, '--repo', repo, '--name', 'Compositor-ZH-preview', '--dir', str(source))
archive = source / 'Compositor-ZH-preview.zip'
expected = (source / 'SHA256SUMS.txt').read_text().split()[0]
actual = hashlib.sha256(archive.read_bytes()).hexdigest()
if actual != expected: raise SystemExit('Build artifact checksum mismatch')
print('Verified input SHA256:', actual, flush=True)
contents = root / 'dist/publish-app'
command('ditto', '-x', '-k', str(archive), str(contents))
app = contents / 'Compositor 中文.app'
info = plistlib.loads((app / 'Contents/Info.plist').read_bytes())
if info['CFBundleIdentifier'] != 'local.compositor.zh' or tag.split('-zh.')[0][1:] != info['CFBundleShortVersionString']:
    raise SystemExit('Application identity/version does not match release tag')
command('codesign', '--verify', '--deep', '--strict', str(app))
# A hosted unit-test run may install its test bundle into the host app.
# It is build infrastructure, not part of the application to distribute.
for test_bundle in app.rglob('*.xctest'):
    print('Remove packaged test bundle:', test_bundle.relative_to(app), flush=True)
    shutil.rmtree(test_bundle)
command('codesign', '--force', '--deep', '--sign', '-', str(app))
command('codesign', '--verify', '--deep', '--strict', str(app))
if list(app.rglob('*.xctest')): raise SystemExit('Test bundle remains in release')
version = tag.split('-zh.')[0][1:]
preview = tag.rsplit('.', 1)[1]
output = root / f'dist/Compositor-ZH-{version}-preview.{preview}.zip'
command('ditto', '-c', '-k', '--sequesterRsrc', '--keepParent', str(app), str(output))
digest = hashlib.sha256(output.read_bytes()).hexdigest()
checksums = root / 'dist/SHA256SUMS.txt'
checksums.write_text(f'{digest}  {output.name}\n')
print('Release SHA256:', digest, flush=True)
notes = root / 'release-notes.md'
command('gh', 'release', 'create', tag, str(output), str(checksums), '--repo', repo,
        '--target', metadata['head_sha'], '--prerelease', '--title', f'Compositor {version} 中文预览版 {preview}', '--notes-file', str(notes))
