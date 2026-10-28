# Compositor 汉化：当前状态

PRIMARY_GOAL：完整可用的简体中文版，并持续跟进官方正式版本。
整体 PARTIAL：代码/构建/相关回归已验证；完整 UI 与实际体验仍须用户截图、人工操作验收。

## 授权及边界

- 用户授权公开仓库 skyyzc/Compositor-ZH、代码修改、云端构建及预览交付。GitHub 连接和 CLI 账号均 skyyzc。
- 不得操作用户桌面或应用：禁止 CUA、open、模拟输入、自动截图、启动/安装程序。仅依据用户主动提供的截图验收。
- 不覆盖 /Applications/Compositor.app；中文预览为独立 local.compositor.zh。
- 只翻译显示边界；不改文档模型、枚举 rawValue、快捷键/功能标识、用户文件名或图层名。构建成功不等于完整目标 VERIFIED。

## 当前基线及交付（2026-10-28）

- 仓库 https://github.com/skyyzc/Compositor-ZH。
- upstream.json 固定官方 1.5.12，提交 fe0a146d1a94476bbe68fb634ae9c31224eabced；官方发布时间 2026-10-27 18:39:20 UTC。
- 汉化代码提交 97c31ced605a729edd545677a88f96b038929e41；831 条词条，保守静态缺词候选 0，不代表完整 UI 覆盖率。本轮补充 11 条译文。
- 最新预览：https://github.com/skyyzc/Compositor-ZH/releases/tag/v1.5.12-zh.preview.1
- ZIP：https://github.com/skyyzc/Compositor-ZH/releases/download/v1.5.12-zh.preview.1/Compositor-ZH-1.5.12-preview.1.zip
- Release asset uploaded，12,539,173 字节；SHA256 cea9b5e9492422f7737152697f73d6e62048335ed1389bb97b2fa28ba9c85f35。Release 同时有 SHA256SUMS.txt。
- 构建 https://github.com/skyyzc/Compositor-ZH/actions/runs/40619047121 success；11 项本地化边界回归及 160 项相关上游测试通过。GitHub job 日志确认 TEST SUCCEEDED，含 7 个轮廓光测试方法；没有执行需单独启用的专用性能基准，不宣称速度倍数已验证。
- 发布 https://github.com/skyyzc/Compositor-ZH/actions/runs/40620029883 success；原始 ZIP 校验、app 版本/标识检查、测试包清理、临时签名/完整性检查、打包上传均成功；gh REST 已确认资产 uploaded。
- 上游项目格式仍为 20；本次新增轮廓光滤镜，不更改官方文档格式与模型。原始 Document 模型和 ProjectStore 与生成副本逐字节一致，不修改官方兼容逻辑。
- 1.5.8 修复的格式 15/16 旧项目读取逻辑继续保留；相关 ProjectTests 仍在回归范围。旧应用可能无法打开新版保存的项目，请使用副本测试；历史预览均保留。

## 实现与证据边界

- TSV 词库为 translations/zh-Hans.tsv；prepare.py + adapt.py 从固定官方快照生成 build-source。
- 当前官方 Document 模型与生成副本逐字节一致；混合模式用 representedObject 保留英文标识，仅显示译名。
- 1.5.7 跟进镜头效果、GIF 时间轴/导出、图层搜索/筛选；工具栏移至 ToolRail.swift，T 图标随迁移适配。
- 首轮构建 40052542437 因上游标题改用 LocalizedStringKey 暴露旧适配器类型冲突；已修复，原生键不经 String 适配，并加入回归。不得回退为盲目包装所有 Text(title)。
- 用户此前截图确认程序可打开、菜单及新建画布宽高/单位中文生效；其余最新界面、编辑/导出体验没有新人工证据。不得将单元测试视为完整 UI 验收。
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
- NEXT：等待用户对 1.5.12 轮廓光及既有界面的截图与实际使用反馈；有官方新版本再继续迁移。未跟踪 default.profraw 为旧会话遗留，不属于源码，未改动或提交。

## 本轮变更 1.5.12（2026-10-28）

- 适配轮廓光新增参数、主体识别提示、动态光源编号及颜色选择器标题，补充 11 条至 831 条词条；11 项本地化检查通过，静态候选 0 不等于完整 UI 覆盖。
- 云端加入 RimLightTests；构建 job 122588293395 日志确认 TEST SUCCEEDED，160 个唯一测试方法通过，包含全部 7 个轮廓光方法。未执行专用性能基准。
- 发布 run 40620029883 success，gh REST 已确认版本化 ZIP 和校验文件 uploaded；tag 指向构建源码 97c31ced605a729edd545677a88f96b038929e41。未重复构建。
- Document 与 ProjectStore 仍保持官方字节，格式仍为 20。无桌面/应用操作，未安装或替换程序，旧预览均保留。整体仍 PARTIAL，新版照片效果、完整中文 UI 和体验待用户人工验收。
