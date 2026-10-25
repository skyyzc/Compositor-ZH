# Compositor 汉化：当前状态

PRIMARY_GOAL：完整可用的简体中文版，并持续跟进官方正式版本。
整体 PARTIAL：代码/构建/相关回归已验证；完整 UI 与实际体验仍须用户截图、人工操作验收。

## 授权及边界

- 用户授权公开仓库 skyyzc/Compositor-ZH、代码修改、云端构建及预览交付。GitHub 连接和 CLI 账号均 skyyzc。
- 不得操作用户桌面或应用：禁止 CUA、open、模拟输入、自动截图、启动/安装程序。仅依据用户主动提供的截图验收。
- 不覆盖 /Applications/Compositor.app；中文预览为独立 local.compositor.zh。
- 只翻译显示边界；不改文档模型、枚举 rawValue、快捷键/功能标识、用户文件名或图层名。构建成功不等于完整目标 VERIFIED。

## 当前基线及交付（2026-10-24）

- 仓库 https://github.com/skyyzc/Compositor-ZH。
- upstream.json 固定官方 1.5.7，提交 9537736da6c324b948cdcba24adf74760498ea14；官方发布时间 2026-10-23 18:06:46 UTC。
- 汉化代码提交 8a921f53cae4822d162ea30cd19200fc8ec36f48；778 条去重词条，保守静态缺词候选 0，不代表完整 UI 覆盖率。
- 最新预览：https://github.com/skyyzc/Compositor-ZH/releases/tag/v1.5.7-zh.preview.1
- ZIP：https://github.com/skyyzc/Compositor-ZH/releases/download/v1.5.7-zh.preview.1/Compositor-ZH-1.5.7-preview.1.zip
- Release asset uploaded，12,284,378 字节；SHA256 2cf61c029b76b340240d8631a60f96cf805cb8117b1d22e4a148aaba8bf28f3e。Release 同时有 SHA256SUMS.txt。
- 构建 https://github.com/skyyzc/Compositor-ZH/actions/runs/40052754864 success；7 项本地化边界回归及 81 项相关上游测试通过。相关测试含 GIF 保存/重开、播放时序、镜头效果、工具栏、图层、通道打包、字体菜单、快捷键、形状、PSD 画板和滤镜。
- 发布 https://github.com/skyyzc/Compositor-ZH/actions/runs/40053341425 success：原始 ZIP 校验，app 版本/标识检查，测试包清理，临时签名及完整性检查，打包上传。
- 上游项目格式已升至 17；旧版可能拒绝新版保存的项目。预览测试使用项目副本，不修改官方兼容逻辑。
- 上一预览 1.5.5：https://github.com/skyyzc/Compositor-ZH/releases/tag/v1.5.5-zh.preview.1，保留用于回退。

## 实现与证据边界

- TSV 词库为 translations/zh-Hans.tsv；prepare.py + adapt.py 从固定官方快照生成 build-source。
- 当前官方 Document 模型与生成副本逐字节一致；混合模式用 representedObject 保留英文标识，仅显示译名。
- 1.5.7 跟进镜头效果、GIF 时间轴/导出、图层搜索/筛选；工具栏移至 ToolRail.swift，T 图标随迁移适配。
- 首轮构建 40052542437 因上游标题改用 LocalizedStringKey 暴露旧适配器类型冲突；已修复，原生键不经 String 适配，并加入回归。不得回退为盲目包装所有 Text(title)。
- 用户此前截图确认程序可打开、菜单及新建画布宽高/单位中文生效；其余最新界面、编辑/导出体验没有新人工证据。不得将 81 项单元测试视为完整 UI 验收。
- 仅临时签名，无 Apple Developer ID 签名或公证。用户截图曾证实 Gatekeeper 拦截，已给出 Apple 官方手动确认说明；不能声称通过 Apple 安全认证。
- 官方更新器启动停用；更新菜单链接项目 Actions。尚无自动安装或回退机制。

## 云端构建与发布

- macos-26 / Xcode 26.6 / Python 3.12；本机不需要完整 Xcode。
- 上游回归使用 build-regression，分发应用使用 build，避免测试包混入。publish-preview.py 仍清理 .xctest 并验签。
- 更新 release-notes.md 后，先确认 Chinese preview 构建成功；通过用户授权的 gh 连接创建指向构建 SHA 的 tag 和预览 Release；再调 publish.yml，输入 run_id 与 tag，云端校验并上传。
- GITHUB_TOKEN 创建 Release 曾遭 403；已验证使用用户连接创建发行记录、云端仅上传资产可行。不得把用户令牌上传为仓库秘密。
- 本机下载曾多次 TLS 超时；使用云端发布，避免下载后再上传。不要因下载问题修改网络或安全设置。

## 持续任务及 NEXT

- automationId=compositor，ACTIVE，每天上海时间 10:00 返回本聊天检查官方正式发行版；版本及待处理状态无变化则保持安静，不重复构建/通知。
- 新版本出现则继续翻译、定向回归和云端构建，仅在新产物、实质失败或必须用户操作时通知。未截图验收的版本仅发布预览；禁止自动替换用户已验收版本。
- 任务涉及本地文件时需电脑开机、Codex 运行。
- NEXT：等待用户对 1.5.7 镜头效果、GIF 时间轴/导出、图层搜索等界面的截图与实际使用反馈；有官方新版本再继续迁移。未跟踪 default.profraw 为旧会话遗留，不属于源码，未改动或提交。

## 当前工作 2026-10-25：官方 1.5.8 迁移

- 检出正式 v1.5.8，2026-10-24 04:48:14 UTC 发布，固定源 8adf15e3b9e421dc1f2e0de28cb190d1fb5b48e2。最新可下载预览暂仍 1.5.7。
- 官方修复 1.5.7 错误拒绝格式 15/16（1.5.4/1.5.5 保存）的项目；保留其 ProjectStore 逻辑，新增逐字节不变检查，云端加入 ProjectTests，含 projectsFromEarlierReleasesStillOpen。
- 棱镜新增单向/双向及模糊说明、阈值说明，新增 8 条词条，共 786 条；8 项本地化边界检查和 FilterSheet 语法解析通过。
- 汉化代码提交 45c7a19689b29d590099ab34945a673a2f379afe，构建 https://github.com/skyyzc/Compositor-ZH/actions/runs/40152691384，结论 success：云端编译、8 项本地化边界检查、94 项相关上游测试通过，包含 ProjectTests/projectsFromEarlierReleasesStillOpen()，准备发布。
- 项目格式仍 17；新 app 读取旧项目修复不意味着旧 app 能读取新版保存项目。原版/已发布预览保留，不操作桌面。
- NEXT：构建成功后创建匹配代码 SHA 的 tag/预览 Release，再调用 publish.yml 云端校验发布；失败则先定位修复，不报告预览可下载。
