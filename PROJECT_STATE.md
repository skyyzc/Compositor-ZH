# Compositor 汉化：当前状态

PRIMARY_GOAL：完整可用的简体中文版，并持续跟进官方正式版本。
整体 PARTIAL：代码/构建/相关回归已验证；完整 UI 与实际体验仍须用户截图、人工操作验收。

## 授权及边界

- 用户授权公开仓库 skyyzc/Compositor-ZH、代码修改、云端构建及预览交付。GitHub 连接和 CLI 账号均 skyyzc。
- 不得操作用户桌面或应用：禁止 CUA、open、模拟输入、自动截图、启动/安装程序。仅依据用户主动提供的截图验收。
- 不覆盖 /Applications/Compositor.app；中文预览为独立 local.compositor.zh。
- 只翻译显示边界；不改文档模型、枚举 rawValue、快捷键/功能标识、用户文件名或图层名。构建成功不等于完整目标 VERIFIED。

## 当前基线及交付（2026-10-25）

- 仓库 https://github.com/skyyzc/Compositor-ZH。
- upstream.json 固定官方 1.5.8，提交 8adf15e3b9e421dc1f2e0de28cb190d1fb5b48e2；官方发布时间 2026-10-24 04:48:14 UTC。
- 汉化代码提交 45c7a19689b29d590099ab34945a673a2f379afe；786 条去重词条，保守静态缺词候选 0，不代表完整 UI 覆盖率。
- 最新预览：https://github.com/skyyzc/Compositor-ZH/releases/tag/v1.5.8-zh.preview.1
- ZIP：https://github.com/skyyzc/Compositor-ZH/releases/download/v1.5.8-zh.preview.1/Compositor-ZH-1.5.8-preview.1.zip
- Release asset uploaded，12,288,887 字节；SHA256 c487cab6a7f21a6f1f4b91c8bbc1d85316e1092d84223f253ed5b86aedab8a2a。Release 同时有 SHA256SUMS.txt。
- 构建 https://github.com/skyyzc/Compositor-ZH/actions/runs/40152691384 success；8 项本地化边界回归及 94 项相关上游测试通过，含 ProjectTests/projectsFromEarlierReleasesStillOpen()（格式 15/16）。
- 发布 https://github.com/skyyzc/Compositor-ZH/actions/runs/40153352474 success：原始 ZIP 校验、app 版本/标识检查、测试包清理、临时签名/完整性检查、打包上传。已通过 GitHub connector 确认成功和 Release assets uploaded。
- 上游项目格式仍为 17；1.5.8 修复 1.5.7 错误拒绝格式 15/16 的兼容性缺陷（影响 1.5.4/1.5.5 保存的项目）。原始 ProjectStore 与生成副本逐字节一致，沿用官方修复，不降级文件格式。
- 旧应用仍可能无法打开新版保存的项目，请使用副本测试；历史预览均保留。

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
- NEXT：等待用户对 1.5.8 棱镜单向/双向/模糊、旧项目打开及既有界面的截图与实际使用反馈；有官方新版本再继续迁移。未跟踪 default.profraw 为旧会话遗留，不属于源码，未改动或提交。

## 本轮变更 1.5.8

- 跟进官方旧项目读取修复；云端加入 ProjectTests，确认格式 15/16 读取回归通过；本地加入 ProjectStore 字节不变检查。
- 棱镜新增单向/双向及模糊控制、阈值说明，补充 8 条词条；无需修改既有显示适配器。
- 无桌面/应用操作。CLI 查询发布状态曾连接失败，改用 GitHub connector 的 fetch_workflow_run_jobs 和 fetch（支持 releases/tags API）确认成功；后续优先复用这些读工具，避免无意义重试。
- 整体仍 PARTIAL，最新 UI、视觉效果、用户真实文件与编辑体验待人工验收。状态无变化时按持续任务保持安静，不重复构建或提醒。

## 当前工作 2026-10-26：官方 1.5.9 迁移

- 检出正式 v1.5.9，2026-10-25 20:59:05 UTC 发布，固定源 efc06ffdf6f93606e59a1f2220fcd64a5d4e0ade。最近已发布预览仍为 1.5.8。
- 新增暗角/镜头效果/局部色调对比调整图层，滤镜菜单重排；复用已有中文词条，无新增词条（786）。新增回归确认提取后的 filterMenuItem 仍调用中文显示翻译；9 项本地检查、CompositorApp 语法解析通过。
- 跟进官方调整图层缓存及 GPU 渲染更新；云端增加 AdjustmentLayerTests、AdjustmentCacheTests、GPUCanvasTests。未运行需要单独启用的专用性能基准，不宣称性能倍数已验证。
- 上游格式升至 18；旧版可能拒绝新版保存项目。Document 模型及 ProjectStore 仍与官方逐字节一致。
- 代码提交 9f0ff6c68c54ce2d49156100cdc4e0ea1504e245；构建 https://github.com/skyyzc/Compositor-ZH/actions/runs/40257650064 success；9 项本地化边界检查及 129 项相关上游测试通过，含 2 项调整缓存和 23 个 GPU 测试方法，未运行专用性能基准。构建/测试成功后创建准确 SHA 的 tag、预览 Release 并调用 publish.yml；未发布前不得通知新包可下载。
- 无桌面/应用操作，最新 UI/渲染观感仍须用户人工验收。
