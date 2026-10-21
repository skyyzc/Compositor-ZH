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

    def test_document_models_unchanged(self):
        for original in (ROOT / 'upstream/Compositor/Document').rglob('*'):
            if original.is_file():
                generated = ROOT / 'build-source/Compositor/Document' / original.relative_to(ROOT / 'upstream/Compositor/Document')
                self.assertEqual(original.read_bytes(), generated.read_bytes(), str(original))

if __name__ == '__main__': unittest.main()
