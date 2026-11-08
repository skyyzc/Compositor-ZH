# Compositor 汉化：当前状态

PRIMARY_GOAL：完整可用的简体中文版，并持续跟进官方正式版本。
整体 PARTIAL：代码/构建/相关回归已验证；完整 UI 与实际体验仍须用户截图、人工操作验收。

## 授权及边界

- 用户授权公开仓库 skyyzc/Compositor-ZH、代码修改、云端构建及预览交付。GitHub 连接和 CLI 账号均 skyyzc。
- 不得操作用户桌面或应用：禁止 CUA、open、模拟输入、自动截图、启动/安装程序。仅依据用户主动提供的截图验收。
- 不覆盖 /Applications/Compositor.app；中文预览为独立 local.compositor.zh。
- 只翻译显示边界；不改文档模型、枚举 rawValue、快捷键/功能标识、用户文件名或图层名。构建成功不等于完整目标 VERIFIED。

## 当前基线及交付（2026-11-08）

- 官方 1.6.6，upstream.json 固定 2f507800bc4b32db6b31d34a822cbfc577bf46cf；汉化源码 c5cf1786f56e285f92b15482d34c155ec41a72ab。
- 885 条词条，静态候选 0；14 项本地化边界检查通过。完整 UI 仍待人工验收。
- 最新预览 https://github.com/skyyzc/Compositor-ZH/releases/tag/v1.6.6-zh.preview.1
- ZIP https://github.com/skyyzc/Compositor-ZH/releases/download/v1.6.6-zh.preview.1/Compositor-ZH-1.6.6-preview.1.zip
- 资产 uploaded，12,898,427 字节；SHA256 86ad27d237ca716c8d6c60ed9cd675174b72ee560352c21edc8cbb05e30b25d3，附 SHA256SUMS.txt。
- 构建 42437083715 success，job 128598123663；TEST SUCCEEDED，38 套件、325 项测试通过（37.137 秒）。新增 BrushRecoveryTests、StrokeEffectTests、ImageSourceTests、CameraRawSliderTests。体积光样图/计时 opt-in 主体未执行。
- 发布 42437701311 success，版本/标识/校验/签名检查及资产上传成功。
- 格式仍为 21，Document、ProjectStore、DepthModel 保持官方字节；项目副本测试。真实模型下载、完整 UI、照片效果与性能体验待人工验收。

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
- NEXT：等待用户对 1.6.6 颜色选择器、画笔恢复、描边及统一滑块的截图与实际使用反馈；有官方新版本再继续迁移。未跟踪 default.profraw 为旧会话遗留，不属于源码，未改动或提交。

## 本轮变更 1.6.3 → 1.6.4（2026-11-05）

- 1.6.3 构建 41757626545 success，尚未发布时官方又发布 1.6.4，因此直接交付新版，无重复构建相同源码。
- 适配减少杂色、间距、新滤镜图层菜单、原生 FooterMenu、色阶动态说明及形状尺寸；1.6.4 再适配选区图标辅助说明和羽化状态文字。883 条词条，14 项本地化边界检查，静态候选 0 不等于完整 UI 覆盖。
- 首轮 1.6.4 构建 41952636447 编译通过，回归出现两项 FloatingPanelTests 失败并在 45 分钟超时取消。xcresult 未完成（无 Info.plist）；只读诊断 41957705781/41957843347 无法解析。不可将该轮视为成功。
- 关闭测试并行、增加单项超时后，41957994722 同范围全部通过，之前失败的浮动面板检查也通过，支持并行测试宿主干扰判断，尚未完整因果隔离。未删测试、放宽断言或修改产品逻辑。保留串行设置；diagnose.yml 可读取完整的既有回归制品，不触发重建。
- 云端增加减少杂色、图层间距、底部布局、魔棒与选区羽化检查。312 项包含参数化测试；体积光样图/计时两个 opt-in 方法未执行主体，不作为照片/性能证据。串行日志格式改为 ✔ Test / ✔ Suite，不能沿用旧 Test case 正则统计成 0。
- 已发布预览，源码 tag 指向 e3019cdda5d3f331a372754a75c5cbf478d5f11f；资产 uploaded。无桌面/应用操作，未安装或替换程序。整体仍 PARTIAL，真实 UI、模型下载及照片效果待人工验收。

## 本轮变更 1.6.6（2026-11-08）

- 复用既有适配，补充颜色选择器两条提示，词库 885。跟进官方画笔恢复、描边、滑块与导出入口调整。快捷键按官方更新保留，未自行改功能标识或用户内容。
- 14 项本地化检查及串行云端相关回归通过，已发布预览。未操作桌面或安装应用。整体 PARTIAL，人工验收缺口继续保留。
