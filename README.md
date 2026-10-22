# Compositor 简体中文维护项目

[下载最新中文预览版（1.5.5）](https://github.com/skyyzc/Compositor-ZH/releases/tag/v1.5.5-zh.preview.1)

基于官方 1.5.5，当前 706 条词条。跟进 RGB 分离、通道打包、字体搜索、线型和压感界面；云端编译、5 项本地化边界检查和 44 项相关上游单元测试通过，界面显示与实际体验仍待人工验收。

注意：上游项目格式已从 14 升至 16，新版保存的 v16 项目无法使用旧版打开。预览测试请使用项目副本。

目标：为本机 Compositor 提供可用的完整中文界面，并在官方更新后持续维护翻译。

当前已跑通云端预览构建，尚未完成完整汉化及功能验收。现有 `/Applications/Compositor.app` 未修改。

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
- `scripts/update.py`：查询官方最新正式发行版并生成 `upstream-status.json`；不会改动固定源版本。
- `translation-status.json`：程序生成的静态翻译候选清单，不能视为完整 UI 覆盖率。
- `PROJECT_STATE.md`：恢复项目的唯一状态入口。

## 持续更新方案与限制

保留官方程序；中文预览使用独立应用标识。汉化修改在生成副本中进行，官方源码可重复获取。禁止翻译存储格式、枚举 rawValue、标识符或用户文档内容。

生成工具停用中文版的官方更新器启动，避免被英文发行版覆盖。中文版更新菜单链接到本仓库的云端构建页，便于下载已构建的预览；它尚不支持自动安装。

已在当前 Codex 聊天配置每天 10:00 跟进官方正式发行版的任务，无变化不通知；涉及本地项目时需电脑开机且应用运行。不自动操作桌面、启动或安装程序。完整交付后可完善：检测正式发行版 → 生成翻译差异 → 翻译新增文字 → 构建与验证 → 切换中文版；遇到无法验证的源码变化应保留旧版并报告。自动发现版本并不意味着新增翻译能够自动获得质量保证。

词库中的动态显示名尚未全部接入本地化；把词条写入目录不等于对应界面已经汉化。必须在完整 Xcode 和运行环境中继续验证。

## 已验证构建

[1.5.3 汉化预览构建](https://github.com/skyyzc/Compositor-ZH/actions/runs/39535444061)已成功，含 587 条词条。产物仍需界面与功能验收；静态候选全部入库不等于所有动态界面已汉化。

## 云端发布

`Publish verified preview` 从成功的构建取得产物，校验、清理测试包、重新临时签名并上传预览 Release。先通过已授权 GitHub 连接创建指向构建 SHA 的 tag 及预览 Release，并更新 `release-notes.md`；再手动运行 `publish.yml`，输入构建 run ID 与预览 tag。工作流不会安装或启动本机应用。
