import pathlib, subprocess, unittest
ROOT = pathlib.Path(__file__).resolve().parents[1]

class LocalizationRegression(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        subprocess.run(['python3', str(ROOT / 'scripts/prepare.py')], check=True)

    def read(self, path):
        return (ROOT / 'build-source/Compositor' / path).read_text()

    def test_screenshot_captions_use_translator(self):
        canvas = self.read('UI/NewCanvasSheet.swift')
        self.assertIn('Text(compositorZh(title))', canvas)  # dimension and CyclePill
        lasso = self.read('UI/LassoControls.swift')
        self.assertIn('Text(compositorZh($0.rawValue)).tag($0)', lasso)
        self.assertIn('Button(compositorZh(title), action: action)', lasso)
        self.assertIn('Text(compositorZh(session.tool == .marquee', lasso)

    def test_blend_mode_uses_stable_identity(self):
        blend = self.read('UI/BlendModePicker.swift')
        self.assertIn('button.lastItem?.representedObject = mode.rawValue', blend)
        self.assertNotIn('LayerBlendMode(rawValue: $0.title)', blend)
        self.assertIn('withTitle: compositorZh(mode.rawValue)', blend)

    def test_filter_and_status_feedback(self):
        app = self.read('CompositorApp.swift')
        self.assertIn('compositorZh("Last Filter")', app)
        self.assertIn('Button(compositorZh("\\(kind.rawValue)…"))', app)
        self.assertIn('Text(compositorZh(session.tool == .marquee', self.read('ContentView.swift'))
        self.assertIn('Text(compositorZh(session.document == nil', self.read('UI/LayersPanel.swift'))
        self.assertIn('tab.session.projectURL == nil ?', self.read('UI/ProjectTabs.swift'))
        terms = dict(line.split('\t') for line in (ROOT / 'translations/zh-Hans.tsv').read_text().splitlines() if line.strip())
        for key in ['Progressive Blur', 'Bloom / Glow', 'Scanlines', 'Tonal Contrast', 'Camera Raw Filter']:
            self.assertIn(key, terms)

    def test_new_release_display_boundaries(self):
        export = self.read('UI/ExportAsSheet.swift')
        self.assertIn('Picker(compositorZh(channel.rawValue),', export)
        self.assertIn('Text(layer.name).tag(ChannelPack.Source.layer(layer.id))', export)
        self.assertIn('Text(compositorZh(format == .channelPack ?', export)
        self.assertIn('compositorZh("Search Fonts")', self.read('UI/FontListPanel.swift'))
        self.assertIn('Button(compositorZh(kind.rawValue + "…"))', self.read('CompositorApp.swift'))
        project = (ROOT / 'build-source/Compositor.xcodeproj/project.pbxproj').read_text()
        self.assertIn('PRODUCT_MODULE_NAME = Compositor;', project)
        self.assertIn('PRODUCT_BUNDLE_IDENTIFIER = com.wonderassembly.compositor.tests;', project)
        self.assertEqual(project.count('PRODUCT_NAME = "Compositor 中文";'), 2)

    def test_document_models_unchanged(self):
        for original in (ROOT / 'upstream/Compositor/Document').rglob('*'):
            if original.is_file():
                generated = ROOT / 'build-source/Compositor/Document' / original.relative_to(ROOT / 'upstream/Compositor/Document')
                self.assertEqual(original.read_bytes(), generated.read_bytes(), str(original))

if __name__ == '__main__': unittest.main()
