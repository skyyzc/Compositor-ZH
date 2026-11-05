# Compositor 汉化：当前状态

PRIMARY_GOAL：完整可用的简体中文版，并持续跟进官方正式版本。
整体 PARTIAL：代码/构建/相关回归已验证；完整 UI 与实际体验仍须用户截图、人工操作验收。

## 授权及边界

- 用户授权公开仓库 skyyzc/Compositor-ZH、代码修改、云端构建及预览交付。GitHub 连接和 CLI 账号均 skyyzc。
- 不得操作用户桌面或应用：禁止 CUA、open、模拟输入、自动截图、启动/安装程序。仅依据用户主动提供的截图验收。
- 不覆盖 /Applications/Compositor.app；中文预览为独立 local.compositor.zh。
- 只翻译显示边界；不改文档模型、枚举 rawValue、快捷键/功能标识、用户文件名或图层名。构建成功不等于完整目标 VERIFIED。

## 当前基线及交付（2026-11-03）

- 仓库 https://github.com/skyyzc/Compositor-ZH。
- upstream.json 固定官方 1.6.1，提交 9b0892b5aea3aabe1e87af2468859a3c32184672；官方发布时间 2026-11-02 20:53:04 UTC。
- 汉化代码提交 ca4d35eb7f4b6b6f006b0344270101f32af0e6f2；869 条词条，本轮新增 38 条；保守静态缺词候选 0，不代表完整 UI 覆盖率。
- 最新预览：https://github.com/skyyzc/Compositor-ZH/releases/tag/v1.6.1-zh.preview.1
- ZIP：https://github.com/skyyzc/Compositor-ZH/releases/download/v1.6.1-zh.preview.1/Compositor-ZH-1.6.1-preview.1.zip
- Release asset uploaded，12,790,752 字节；SHA256 09081f0d3a70212bae00014c1e6b4eea0cd48a85feaeb51c9db542fab45f723b。Release 同时有 SHA256SUMS.txt。
- 构建 https://github.com/skyyzc/Compositor-ZH/actions/runs/41564126429 success，job 125681406194 日志 TEST SUCCEEDED；13 项本地化检查通过，289 个唯一上游测试方法记录通过。体积光样图/计时两个 opt-in 方法提前返回，未执行其主体；不作为效果/性能证据。
- 发布 https://github.com/skyyzc/Compositor-ZH/actions/runs/41565192670 success；原始 ZIP 校验、app 版本/标识检查、测试包清理、临时签名/完整性检查、打包上传成功；gh REST 确认资产 uploaded。
- 项目格式仍为 20；Document、ProjectStore、DepthModel 与生成副本逐字节一致，不修改官方兼容逻辑、深度模型来源/哈希和文件名函数。旧应用可能无法打开新版保存的项目，请使用副本测试；历史预览均保留。
- 官方体积光首次使用下载约 2.6 MB 深度模型。本次回归覆盖等待/失败回退等逻辑，未验证真实网络下载、照片视觉效果或专用性能基准。

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
- NEXT：等待用户对 1.6.1 体积光、提取深度、PNG 图层导出、多选及右键菜单的截图与实际使用反馈；有官方新版本再继续迁移。未跟踪 default.profraw 为旧会话遗留，不属于源码，未改动或提交。

## 本轮变更 1.6.1（2026-11-03）

- 新增体积光、深度提取与参数/提示、PNG 图层导出、多选图层菜单、原生右键菜单及选区尺寸显示汉化；用户文件名与图层名保持原始值。
- 原生菜单标题仅显示时翻译；Add Mask 的标题验证比较同步使用译文，动作 selector/启用条件不变。
- 首轮构建 41563358762 编译成功、回归失败：4 个 LayerTests 菜单断言硬编码英文。已仅在生成的测试副本适配显示断言，并增加运行时 Add Mask → 添加蒙版检查；保留动作、启用条件、撤销和模型断言。13 项本地化检查与修复后云端回归通过。
- 云端加入 VolumetricLightTests、LayerExportTests、DeepLayerTests、HistoryTests、ImageSizeTests、LayerAppearanceTests、LayerTests、LiveMaskTests、SelectionTests，确认本轮相关逻辑。289 方法记录包含两个未启用的体积光样图/计时方法，不宣称真实照片效果或性能验证。
- 无桌面/应用操作，未安装或替换程序。整体仍 PARTIAL，新版完整中文 UI、真实模型下载及体验待用户人工验收。

## 当前工作 1.6.3（2026-11-04）

- 官方 1.6.3 发布于 2026-11-03 21:30:23 UTC，固定 5c3489e84c2d22da18566f40079f14f86296e57c；汉化提交 692602a97c6e38530e742e218d91e3634cd079c4。
- 新增减少杂色、间距、滤镜图层菜单，补充 11 条至 880 词条；适配重构后的原生 FooterMenu 与色阶动态说明、形状尺寸文字，14 项本地化检查通过，静态候选 0。
- 云端构建 https://github.com/skyyzc/Compositor-ZH/actions/runs/41757626545 已提交，增加 ReduceNoiseTests、LayerDistancesTests、LayersFooterTests、MagicWandTests。Document/ProjectStore/DepthModel 保持官方字节，格式升至 21。
- NEXT：确认构建/回归后发布预览，发布前可下载版本仍为 1.6.1；实际中文 UI/照片效果仍待人工验收。

## 当前工作 1.6.4（2026-11-05）

- 已确认 1.6.3 构建 41757626545 success，尚未发布；官方随后发布 1.6.4（2026-11-05 01:16:20 UTC），直接继续迁移新版，避免交付过时预览。
- 固定 f2add91afe7a63d789cf096cca34b797c4c0f0f7；汉化源码 08eb18474f99ebc7608232bd75d42c1f30733699。新增 3 条词条共 883；适配重构后的选区图标辅助标签和羽化状态文字，14 项本地化检查通过，静态候选 0。
- 云端构建 https://github.com/skyyzc/Compositor-ZH/actions/runs/41952636447 进行中，增加 SelectionFeatherTests；格式仍为 21。NEXT：确认回归后发布新版预览，当前可下载基线仍为 1.6.1。

- 1.6.4 首轮 41952636447 编译通过，回归超时取消；日志记录 FloatingPanelTests 的 dockedPlacementLeavesTheSavedFilterPosition、cameraRawDocksToTheDocumentWindow 失败，根因尚 UNKNOWN。并行宿主在同一云端桌面运行，为可能干扰来源，不能直接认定为产品或汉化错误。
- 超时留下的 xcresult 未完成（无 Info.plist），云端只读诊断 41957705781/41957843347 无法解析；不据此升级验证状态。已关闭测试并行并启用 120–180 秒单项超时，完整保留原回归范围重新验证。
