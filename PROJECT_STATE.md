# 当前状态

PRIMARY_GOAL：完整汉化本机 Compositor，并持续跟随官方更新维护汉化。

整体状态：PARTIAL；已采用 GitHub 云端构建，本机缺少 Xcode 不再是必要阻塞。云端构建和运行尚待验证。

## VERIFIED

- 安装路径 `/Applications/Compositor.app`；版本 1.5.3 / build 49；arm64 原生 SwiftUI/AppKit 应用。
- 安装包 Resources 没有现成 `.lproj` / `.strings` 语言资源，不能靠切换系统语言完成汉化。
- 官方源码 MIT 开源，目前 README 明确只支持英文且不接受翻译 PR。
- 官方源码快照 `365b5745eda537f984f3d5bed1e53c361dbc9c91`，与 1.5.3 发布对应。
- 本机仅 `/Library/Developer/CommandLineTools`，无完整 Xcode。
- `scripts/prepare.py` 已运行，生成 287 条去重词条的字符串目录，发现 300 条未译静态候选。
- 原安装未修改；没有安装后台任务。

## IMPLEMENTED_NOT_VERIFIED

- 独立 TSV 词库、可重复生成源码与字符串目录、独立 Bundle ID / 产品名。
- 生成时停用官方更新器启动，定位不匹配时终止。
- 构建预览、本地签名、显式跟进官方 main 的脚本。

## 缺口

- 至少 300 条静态候选未翻译；动态字符串、AppKit 控件、撤销历史、命令搜索显示名需要定向适配。
- 禁止直接改枚举 rawValue；部分混合模式控件会把显示标题转回枚举，需将标识与显示分离。
- 尚未构建或启动汉化版本；菜单、布局、保存/加载、快捷键、图像处理、导出均未验收。
- 自动检测正式版本、翻译新增内容、保留旧版/回退和后台更新机制尚未完成。
- “检查更新”菜单应替换为中文版维护入口，当前生成版停用其 updater 启动但菜单仍在。

## GitHub 路线

- 用户已授权公开仓库；账号 skyyzc。
- 仓库 https://github.com/skyyzc/Compositor-ZH 已创建。
- 已准备固定源提交的云端构建流程，上传前通过 Python 语法检查及 Xcode 项目 plist 语法检查。
- 没有 Apple 开发者签名/公证；预览采用临时签名。

## NEXT

上传并跑通 GitHub Actions，修复构建问题，继续翻译及动态 UI / AppKit 适配；下载产物后在本机运行验收。完成首版后完善正式发行跟进和中文更新流程。不得把预览报告为完整汉化。
