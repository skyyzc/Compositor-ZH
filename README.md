# Compositor 简体中文维护项目

[下载 1.5.11 中文预览版](https://github.com/skyyzc/Compositor-ZH/releases/tag/v1.5.11-zh.preview.1)

基于官方 Compositor 1.5.11，当前 820 条词条，跟进镜头效果、GIF 时间轴与导出、图层搜索等界面。云端编译、10 项本地化边界检查及 153 项相关上游测试通过；实际中文布局和使用体验仍待人工验收，不宣称已完整汉化。

1.5.11 补充自定义裁剪比例、图层对齐/分布、锐化调整图层及棱镜色散的汉化；保留官方镜头效果蒙版、颜色选择器与平移光标修复。相关回归通过，未执行专用性能基准。

## 使用

解压 ZIP，退出旧中文版后运行“Compositor 中文.app”。应用可独立运行，无需 Xcode。建议保留官方原版和旧预览。上游项目格式已升至 20，旧版可能无法打开新版保存的项目；预览请使用项目副本。

应用目前仅临时签名，未经 Apple Developer ID 签名或公证。首次打开可能触发 macOS 安全提示，由用户依据 [Apple 官方说明](https://support.apple.com/zh-cn/102445)自行决定是否继续。

## 维护方式

- `upstream.json` 固定官方正式版本提交；`scripts/fetch-source.py` 获取源码。
- `translations/zh-Hans.tsv` 是独立词库；`scripts/prepare.py` 与 `scripts/adapt.py` 生成汉化源码和原生字符串目录。
- `tests/test_localization.py` 检查显示边界、内部标识与模型保留；云端还运行相关上游单元测试。
- `Chinese preview` 工作流编译、测试并打包。用户本机不需要 Xcode。
- `Publish verified preview` 工作流校验已有成功构建、检查应用版本/标识、清理测试包、重新临时签名并上传预览发行记录。先通过已授权 GitHub 连接创建指向构建 SHA 的 tag 与预览 Release，更新 `release-notes.md`，再运行 `publish.yml` 输入构建 run ID 和 tag。
- `scripts/update.py` 检查官方最新正式版，不改变固定源版本。
- `PROJECT_STATE.md` 是项目当前状态与验证证据的唯一入口。

已配置每天 10:00 在本 Codex 聊天持续跟进官方版本的任务，无变化不通知；涉及本地文件时需电脑开机、Codex 运行。维护过程不操作用户桌面或应用，界面验收由用户提供截图。目前不自动安装或替换本机应用。

保留官方程序。中文版本使用独立标识；官方更新器启动已停用，更新入口指向本项目，避免被英文发行版覆盖。文档模型、枚举原始值、快捷键及用户文件名/图层名保持官方行为。

上游项目采用 MIT 许可，原作者版权及许可见 LICENSE。
