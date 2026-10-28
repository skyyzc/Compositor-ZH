基于官方 Compositor 1.5.12 的简体中文预览版 1。

- 跟进新增的轮廓光（Rim Light）滤镜，补充主体识别、辉光、光源颜色/角度/强度/宽度/边缘控制等中文说明。
- 适配动态光源编号与颜色选择器标题，保留光源 ID、模型及官方滤镜逻辑。
- 词库增至 831 条；静态缺词候选 0 不代表完整 UI 覆盖。

云端编译、11 项本地化边界检查及 160 项相关上游测试通过，包含 7 项轮廓光测试。构建证据：https://github.com/skyyzc/Compositor-ZH/actions/runs/40619047121 。实际中文布局、照片效果及编辑体验仍待用户人工验收，不宣称完整汉化 VERIFIED，未执行专用性能基准。

兼容性：官方项目格式仍为 20；旧应用可能无法打开新版保存的项目。请使用项目副本测试，保留旧版及官方原版。

下载 Assets 中 Compositor-ZH-1.5.12-preview.1.zip，退出旧中文版后解压运行，无需 Xcode。仅临时签名，无 Apple Developer ID 签名或公证，首次打开可能需要用户手动确认。未操作用户桌面，未安装或启动本机应用。

官方发行说明：https://github.com/robbietilton/Compositor/releases/tag/v1.5.12
