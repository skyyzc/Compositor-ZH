# 当前状态

PRIMARY_GOAL：完整汉化本机 Compositor，并持续跟随官方更新维护汉化。

整体状态：PARTIAL。GitHub 云端构建路线 VERIFIED；UI 与功能验收尚未完成。

## 已验证基线

- 原安装 `/Applications/Compositor.app`：1.5.3 / build 49，未修改。
- 原生 SwiftUI/AppKit；官方无现成语言包，源码 MIT 开源，暂不接受翻译 PR。
- 固定官方提交 `365b5745eda537f984f3d5bed1e53c361dbc9c91`，配置在 upstream.json。
- 用户选择第三种路线：GitHub 管理源码并云端构建，本机无需 Xcode；明确授权公开仓库。
- GitHub 连接及 CLI 登录账号均为 skyyzc。仓库 https://github.com/skyyzc/Compositor-ZH。
- 已上传 587 条去重中文词条；当前保守扫描的静态 UI 候选未译数 0。不是完整 UI 覆盖率。
- 云端构建提交 `860ef930cdec0fd2f1bdc646c402bb24d229ca47`：https://github.com/skyyzc/Compositor-ZH/actions/runs/39535444061，结论 success。
- macos-26 / Xcode 26.6 / Python 3.12 已成功构建、临时签名和打包；本机也通过 codesign --verify --deep --strict。
- ZIP SHA256：b64af90ca33273453f2594e6ff4ba97f685d963ddd9c42b1e298f6b3656882ff，与云端清单一致。
- 产物：dist/Compositor-ZH-preview.zip；解压应用 dist/preview/Compositor 中文.app。
- 系统启动请求成功，CUA 应用清单确认 local.compositor.zh isRunning=true。
- 官方最新正式发行版查询仍为 v1.5.3；scripts/update.py 已执行验证，不改变固定源提交。

## IMPLEMENTED_NOT_VERIFIED / 缺口

- 原生字符串目录已打包，中文资源存在；动态文字与 AppKit 控件尚待完整适配。
- CUA getApp(local.compositor.zh) 连续超时（42 秒、60 秒）；无法读取窗口树或截图，因此不能声称中文 UI、布局及功能 VERIFIED。
- 第一次在沙盒内 open 返回 -10827，直接执行返回 134；改为获批的桌面 open 后成功，应用清单确认运行。不要将沙盒启动失败推断为构建产物损坏。
- 预览用独立 Bundle ID / 产品名；官方更新器启动已停用，更新菜单改为打开本仓库 Actions。
- 未经 Apple Developer ID 签名与公证；仅预览产物。
- 混合模式等控件用显示标题转回枚举，后续需将标识与译名分离；不得改枚举 rawValue / 存储格式。
- 保存/加载、快捷键、图像处理、导出均未验收。
- 后台监控、自动翻译新增文字、正式发行及自动安装/回退机制尚未完成。

## NEXT

优先取得实际窗口证据（CUA 若持续超时需用户确认窗口状态），适配动态 UI / AppKit 并进行新建、导入、保存、重开、导出和快捷键验收。首个可用版本通过后，再接入正式版本自动跟进与安全更新。云端构建成功不等于完整汉化完成。
