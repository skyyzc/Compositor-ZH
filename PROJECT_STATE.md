# Compositor 汉化：当前状态

PRIMARY_GOAL：完整可用的简体中文版，并持续跟进官方正式版本。
整体 PARTIAL：代码/构建/相关回归已验证；完整 UI 与实际体验仍须用户截图、人工操作验收。

## 授权及边界

- 用户授权公开仓库 skyyzc/Compositor-ZH、代码修改、云端构建及预览交付。GitHub 连接和 CLI 账号均 skyyzc。
- 不得操作用户桌面或应用：禁止 CUA、open、模拟输入、自动截图、启动/安装程序。仅依据用户主动提供的截图验收。
- 不覆盖 /Applications/Compositor.app；中文预览为独立 local.compositor.zh。
- 只翻译显示边界；不改文档模型、枚举 rawValue、快捷键/功能标识、用户文件名或图层名。构建成功不等于完整目标 VERIFIED。

## 当前基线及交付（2026-11-05）

- 仓库 https://github.com/skyyzc/Compositor-ZH。
- upstream.json 固定官方 1.6.4，提交 f2add91afe7a63d789cf096cca34b797c4c0f0f7；官方发布时间 2026-11-05 01:16:20 UTC。
- 汉化代码提交 e3019cdda5d3f331a372754a75c5cbf478d5f11f；883 条词条，包含 1.6.3 新增 11 条及 1.6.4 新增 3 条；保守静态缺词候选 0，不代表完整 UI 覆盖率。
- 最新预览：https://github.com/skyyzc/Compositor-ZH/releases/tag/v1.6.4-zh.preview.1
- ZIP：https://github.com/skyyzc/Compositor-ZH/releases/download/v1.6.4-zh.preview.1/Compositor-ZH-1.6.4-preview.1.zip
- Release asset uploaded，12,858,706 字节；SHA256 7d593a6e4f66abc8df042abacea7ec2281494efac96da62be969d9cd412ce4b5。Release 同时有 SHA256SUMS.txt。
- 构建 https://github.com/skyyzc/Compositor-ZH/actions/runs/41957994722 success，job 127017392098 日志 TEST SUCCEEDED；14 项本地化检查通过；串行回归日志确认 34 套件、312 项测试通过（51.957 秒）。体积光样图/计时两个 opt-in 方法提前返回，未执行其主体；不作为效果/性能证据。
- 发布 https://github.com/skyyzc/Compositor-ZH/actions/runs/41959147158 success；原始 ZIP 校验、app 版本/标识检查、测试包清理、临时签名/完整性检查、打包上传成功；gh REST 确认资产 uploaded。
- 项目格式升至 21；Document、ProjectStore、DepthModel 与生成副本逐字节一致，不修改官方兼容逻辑、深度模型来源/哈希和文件名函数。旧应用可能无法打开新版保存的项目，请使用副本测试；历史预览均保留。
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
- 回归串行运行（-parallel-testing-enabled NO），单项超时 120–180 秒；避免多个测试宿主同时操作全局 AppKit 窗口。上游回归使用 build-regression，分发应用使用 build，避免测试包混入。publish-preview.py 仍清理 .xctest 并验签。
- 更新 release-notes.md 后，先确认 Chinese preview 构建成功；通过用户授权的 gh 连接创建指向构建 SHA 的 tag 和预览 Release；再调 publish.yml，输入 run_id 与 tag，云端校验并上传。
- GITHUB_TOKEN 创建 Release 曾遭 403；已验证使用用户连接创建发行记录、云端仅上传资产可行。不得把用户令牌上传为仓库秘密。
- 本机下载曾多次 TLS 超时；使用云端发布，避免下载后再上传。不要因下载问题修改网络或安全设置。

## 持续任务及 NEXT

- automationId=compositor，ACTIVE，每天上海时间 10:00 返回本聊天检查官方正式发行版；版本及待处理状态无变化则保持安静，不重复构建/通知。
- 新版本出现则继续翻译、定向回归和云端构建，仅在新产物、实质失败或必须用户操作时通知。未截图验收的版本仅发布预览；禁止自动替换用户已验收版本。
- 任务涉及本地文件时需电脑开机、Codex 运行。
- NEXT：等待用户对 1.6.4 减少杂色、图层底部菜单、间距及选区图标/羽化状态的截图与实际使用反馈；有官方新版本再继续迁移。未跟踪 default.profraw 为旧会话遗留，不属于源码，未改动或提交。

## 本轮变更 1.6.3 → 1.6.4（2026-11-05）

- 1.6.3 构建 41757626545 success，尚未发布时官方又发布 1.6.4，因此直接交付新版，无重复构建相同源码。
- 适配减少杂色、间距、新滤镜图层菜单、原生 FooterMenu、色阶动态说明及形状尺寸；1.6.4 再适配选区图标辅助说明和羽化状态文字。883 条词条，14 项本地化边界检查，静态候选 0 不等于完整 UI 覆盖。
- 首轮 1.6.4 构建 41952636447 编译通过，回归出现两项 FloatingPanelTests 失败并在 45 分钟超时取消。xcresult 未完成（无 Info.plist）；只读诊断 41957705781/41957843347 无法解析。不可将该轮视为成功。
- 关闭测试并行、增加单项超时后，41957994722 同范围全部通过，之前失败的浮动面板检查也通过，支持并行测试宿主干扰判断，尚未完整因果隔离。未删测试、放宽断言或修改产品逻辑。保留串行设置；diagnose.yml 可读取完整的既有回归制品，不触发重建。
- 云端增加减少杂色、图层间距、底部布局、魔棒与选区羽化检查。312 项包含参数化测试；体积光样图/计时两个 opt-in 方法未执行主体，不作为照片/性能证据。串行日志格式改为 ✔ Test / ✔ Suite，不能沿用旧 Test case 正则统计成 0。
- 已发布预览，源码 tag 指向 e3019cdda5d3f331a372754a75c5cbf478d5f11f；资产 uploaded。无桌面/应用操作，未安装或替换程序。整体仍 PARTIAL，真实 UI、模型下载及照片效果待人工验收。
