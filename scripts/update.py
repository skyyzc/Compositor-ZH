#!/usr/bin/env python3
"""Check the latest official release without changing the pinned build source."""
import json, pathlib, urllib.request
root = pathlib.Path(__file__).resolve().parents[1]
current = json.loads((root / 'upstream.json').read_text())
request = urllib.request.Request('https://api.github.com/repos/robbietilton/Compositor/releases/latest', headers={'Accept': 'application/vnd.github+json', 'User-Agent': 'Compositor-ZH'})
with urllib.request.urlopen(request, timeout=30) as response:
    release = json.load(response)
report = {'current_version': current['version'], 'latest_version': release['tag_name'].removeprefix('v'), 'url': release['html_url']}
report['update_available'] = report['current_version'] != report['latest_version']
(root / 'upstream-status.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(report, ensure_ascii=False, indent=2))
if report['update_available']:
    print('发现新版本；固定源版本保持不变，需检查翻译差异并验证后再升级。')
