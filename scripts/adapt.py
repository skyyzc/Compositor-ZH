"""Localize display boundaries while preserving model values and document identifiers."""
import re

def apply(output):
    helper = '''import Foundation

/// Resolve UI labels in the Chinese catalog; never use for identifiers or user content.
nonisolated func compositorZh(_ value: String) -> String {
    guard let path = Bundle.main.path(forResource: "zh-Hans", ofType: "lproj"),
          let bundle = Bundle(path: path) else { return value }
    let translated = bundle.localizedString(forKey: value, value: value, table: "Localizable")
    if translated != value { return translated }
    if value.hasSuffix("…") {
        let base = String(value.dropLast())
        return bundle.localizedString(forKey: base, value: base, table: "Localizable") + "…"
    }
    return value
}
'''
    (output / 'Compositor/UI/ChineseLocalization.swift').write_text(helper)
    changes = {}
    for path in (output / 'Compositor/UI').glob('*.swift'):
        if path.name == 'ChineseLocalization.swift': continue
        original = text = path.read_text()
        # Enum values are translated only at rendering; Picker tags remain their original types.
        text = re.sub(r'Text\(([^()\n]*\.rawValue)\)', r'Text(compositorZh(\1))', text)
        # These exact helper arguments are fixed UI captions, not document / layer names.
        text = text.replace('Text(title)', 'Text(compositorZh(title))')
        if path.name in {'TransformInspector.swift', 'ColorPickerSheet.swift'}:
            text = text.replace('Text(label)', 'Text(compositorZh(label))')
        text = text.replace('Button(title, action:', 'Button(compositorZh(title), action:')
        text = text.replace('.help(help)', '.help(compositorZh(help))')
        if path.name == 'LassoControls.swift':
            text = text.replace('Text(session.tool == .marquee ? "Marquee" : session.tool == .wand ? "Magic" : "Lasso")', 'Text(compositorZh(session.tool == .marquee ? "Marquee" : session.tool == .wand ? "Magic" : "Lasso"))')
        # These are enum/preset captions, not arbitrary user-provided names.
        if path.name in {'LassoControls.swift', 'NewCanvasSheet.swift'}:
            text = text.replace('Text($0.title)', 'Text(compositorZh($0.title))')
        if text != original:
            path.write_text(text)
            changes[str(path.relative_to(output))] = sum(a != b for a, b in zip(original.splitlines(), text.splitlines()))
    path = output / 'Compositor/UI/BlendModePicker.swift'
    text = path.read_text()
    needle = 'for mode in group { button.addItem(withTitle: mode.rawValue) }'
    if text.count(needle) != 1: raise SystemExit('Blend mode menu changed; review required.')
    text = text.replace(needle, '''for mode in group {
                button.addItem(withTitle: compositorZh(mode.rawValue))
                button.lastItem?.representedObject = mode.rawValue
            }''')
    text = text.replace('LayerBlendMode(rawValue: $0.title)', '($0.representedObject as? String).flatMap { LayerBlendMode(rawValue: $0) }')
    text = text.replace('withTitle: (session.activeLayer?.blendMode ?? .normal).rawValue', 'withTitle: compositorZh((session.activeLayer?.blendMode ?? .normal).rawValue)')
    text = text.replace('withTitle: mode.rawValue', 'withTitle: compositorZh(mode.rawValue)')
    path.write_text(text)
    # Dynamic menu titles bypass SwiftUI's literal-key overload as well.
    path = output / 'Compositor/CompositorApp.swift'
    text = path.read_text()
    for expression in [
        'session.isMaskSelected ? "Invert Mask" : "Invert"',
        'kind.rawValue + (kind.isEditable ? "…" : "")',
        '"\\(kind.rawValue)…"',
    ]:
        text = text.replace('Button(' + expression + ')', 'Button(compositorZh(' + expression + '))')
    path.write_text(text)
    text = text.replace('session.lastFilter.map { "Last Filter: " + $0.rawValue } ?? "Last Filter"', 'session.lastFilter.map { compositorZh("Last Filter") + "：" + compositorZh($0.rawValue) } ?? compositorZh("Last Filter")')
    path.write_text(text)
    path = output / 'Compositor/ContentView.swift'
    text = path.read_text()
    lines = text.splitlines()
    for index, line in enumerate(lines):
        if 'Text(session.tool == .marquee ?' in line:
            lines[index] = line.replace('Text(', 'Text(compositorZh(', 1) + ')'
    text = '\n'.join(lines) + '\n'
    text = text.replace('else if tool == .cloneStamp', 'else if tool == .type { Text("T").font(.system(size: 17, weight: .medium)) }\n                        else if tool == .cloneStamp')
    path.write_text(text)
    path = output / 'Compositor/UI/LayersPanel.swift'
    text = path.read_text().replace('Text(session.document == nil ? "Create a canvas or import an image." : "Import an image or add a blank layer.")', 'Text(compositorZh(session.document == nil ? "Create a canvas or import an image." : "Import an image or add a blank layer."))')
    path.write_text(text)
    path = output / 'Compositor/UI/ProjectTabs.swift'
    text = path.read_text().replace('Text(tab.title)', 'Text(tab.session.projectURL == nil ? tab.title.replacingOccurrences(of: "Untitled", with: "未命名", options: .anchored) : tab.title)')
    path.write_text(text)
    # Native dialog captions use String, not LocalizedStringKey.
    for path in (output / 'Compositor/IO').glob('*.swift'):
        if path.name == 'UpdateDriver.swift': continue  # Official updater is inactive.
        text = path.read_text()
        text = re.sub(r'(\.(?:title|messageText|informativeText) = )("[^"\\\n]*")(?=\s*$)', r'\1compositorZh(\2)', text, flags=re.MULTILINE)
        text = re.sub(r'(addButton\(withTitle: )("[^"\\\n]*")\)', r'\1compositorZh(\2))', text)
        path.write_text(text)
    return changes
