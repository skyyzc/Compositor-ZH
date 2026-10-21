#!/usr/bin/env python3
"""Recreate a localized source tree without editing the upstream checkout."""
import json, pathlib, re, shutil, subprocess, sys, tarfile, io
ROOT = pathlib.Path(__file__).resolve().parents[1]
source = ROOT / 'upstream'
output = ROOT / 'build-source'
translations = {}
for number, line in enumerate((ROOT / 'translations/zh-Hans.tsv').read_text().splitlines(), 1):
    if not line.strip(): continue
    key, value = line.split('\t')
    if key in translations and translations[key] != value:
        raise SystemExit(f'Conflicting translation on line {number}: {key}')
    translations[key] = value
if output.exists(): shutil.rmtree(output)
output.mkdir()
archive = subprocess.check_output(['git', '-C', str(source), 'archive', 'HEAD'])
with tarfile.open(fileobj=io.BytesIO(archive)) as bundle:
    bundle.extractall(output, filter='data')
strings = {key: {'extractionState': 'manual', 'localizations': {'zh-Hans': {'stringUnit': {'state': 'translated', 'value': value}}}} for key, value in sorted(translations.items())}
(output / 'Compositor/Localizable.xcstrings').write_text(json.dumps({'sourceLanguage': 'en', 'strings': strings, 'version': '1.0'}, ensure_ascii=False, indent=2) + '\n')
# Keep official updates from replacing a locally compiled Chinese edition.
delegate = output / 'Compositor/IO/CompositorApplicationDelegate.swift'
text = delegate.read_text()
needle = 'do { try self?.updater.start() } catch { NSLog("Sparkle didn\'t start: \\(error)") }'
if text.count(needle) != 1:
    raise SystemExit('Upstream updater changed; review required before building.')
text = text.replace(needle, '// Chinese edition updates are built by the external update script.')
delegate.write_text(text)
app_source = output / 'Compositor/CompositorApp.swift'
app_text = app_source.read_text()
update_button = 'Button("Check for Updates…") { applicationDelegate.updater.checkForUpdates() }'
if app_text.count(update_button) != 1:
    raise SystemExit('Upstream update menu changed; review required.')
app_text = app_text.replace(update_button, 'Button("中文版下载与更新…") { NSWorkspace.shared.open(URL(string: "https://github.com/skyyzc/Compositor-ZH/actions/workflows/build.yml")!) }')
app_source.write_text(app_text)
# Only isolate app identity; never translate enum raw values / serialization strings.
project = output / 'Compositor.xcodeproj/project.pbxproj'
text = project.read_text().replace('PRODUCT_BUNDLE_IDENTIFIER = com.wonderassembly.compositor;', 'PRODUCT_BUNDLE_IDENTIFIER = local.compositor.zh;')
text = text.replace('STRING_CATALOG_GENERATE_SYMBOLS = YES;', 'STRING_CATALOG_GENERATE_SYMBOLS = NO;')
text = text.replace('PRODUCT_NAME = "$(TARGET_NAME)";', 'PRODUCT_NAME = "Compositor 中文";')
project.write_text(text)
# Discover conservative static UI candidates; dynamic strings require a separate review.
pattern = re.compile(r'(?:Text|Button|Menu|CommandMenu|Toggle|Picker|Label|TextField|SecureField|GroupBox|Section|Window|\.help|\.navigationTitle|\.accessibilityLabel)\(\s*"((?:[^"\\]|\\.)*)"')
found = {}
for path in (output / 'Compositor').rglob('*.swift'):
    for match in pattern.finditer(path.read_text()):
        value = match.group(1)
        if '\\' in value or not re.search('[A-Za-z]', value): continue
        if value not in translations:
            found.setdefault(value, []).append(str(path.relative_to(output)))
report = {'upstream_commit': subprocess.check_output(['git', '-C', str(source), 'rev-parse', 'HEAD'], text=True).strip(), 'dictionary_entries': len(translations), 'untranslated_static_candidates': found, 'limitations': ['Static SwiftUI catalog only; dynamic labels and AppKit text still require adaptation.', 'Build and runtime verification require full Xcode.']}
(ROOT / 'translation-status.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
print(f'Prepared {len(translations)} translations; {len(found)} untranslated static candidates. See translation-status.json.')
if '--require-complete' in sys.argv and found: sys.exit(2)
