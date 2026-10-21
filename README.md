# Compositor 简体中文维护项目

目标：为本机 Compositor 提供可用的完整中文界面，并在官方更新后持续维护翻译。

当前为准备阶段，尚未交付可运行的完整中文版。现有 `/Applications/Compositor.app` 未修改。

## 云端构建（当前采用）

仓库：https://github.com/skyyzc/Compositor-ZH

GitHub Actions 在 macOS 环境生成部分汉化预览，本机不需要安装 Xcode。在仓库 Actions → Chinese preview 中查看构建；成功后下载 `Compositor-ZH-preview` 产物。

预览程序为本地临时签名，尚未经过 Apple 开发者签名与公证；当前用于功能验收，尚非正式发行版。请保留官方应用。

`upstream.json` 固定官方提交，构建不会静默使用最新 main。修改固定提交前必须核对版本与翻译差异。`python3 scripts/fetch-source.py` 获取该提交；本地若有完整 Xcode，也可运行 `python3 scripts/build.py`。

## 文件

- `translations/zh-Hans.tsv`：独立、可维护的英文 → 简体中文词库。
- `upstream/`：官方源码快照。不要在这里修改译文。
- `scripts/prepare.py`：从官方 Git 快照生成 `build-source/` 和原生字符串目录，列出新增未译静态文字。
- `scripts/build.py`：检查 Xcode、生成源码、构建并本地签名预览。产物在 `build/Build/Products/Debug/`。
- `scripts/update.py`：显式获取官方 main 最新提交并重新生成；有未译候选时以失败状态退出，避免误报已完成更新。main 不一定是正式发行版本，正式升级前需核对版本。
- `translation-status.json`：程序生成的静态翻译候选清单，不能视为完整 UI 覆盖率。
- `PROJECT_STATE.md`：恢复项目的唯一状态入口。

## 持续更新方案与限制

保留官方程序；中文预览使用独立应用标识。汉化修改在生成副本中进行，官方源码可重复获取。禁止翻译存储格式、枚举 rawValue、标识符或用户文档内容。

生成工具停用中文版的官方更新器启动，避免被英文发行版覆盖。中文版“检查更新”菜单目前仍待替换成中文维护流程入口，不能视为已实现的更新功能。

目前没有安装后台监控或无人值守自动更新。完整交付后可增加：检测正式发行版 → 生成翻译差异 → 翻译新增文字 → 构建与验证 → 切换中文版；遇到无法验证的源码变化应保留旧版并报告。自动发现版本并不意味着新增翻译能够自动获得质量保证。

词库中的动态显示名尚未全部接入本地化；把词条写入目录不等于对应界面已经汉化。必须在完整 Xcode 和运行环境中继续验证。
