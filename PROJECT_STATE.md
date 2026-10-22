# Compositor 汉化：当前状态

PRIMARY_GOAL：提供完整可用的简体中文版，持续随官方正式版本维护。
整体状态 PARTIAL；云端构建路线已跑通，界面和功能采用用户截图/人工验收。

## 执行边界

用户已授权公开 GitHub 仓库、代码修改、云端构建和预览交付。禁止操作用户桌面/应用：不得 CUA、open、模拟输入、自动截图、启动或安装程序。用户人工提供截图。
不要改文档格式、模型枚举 rawValue 或用户文件名；只翻译显示边界。构建通过不等于 UI 或编辑功能 VERIFIED。

## SSOT 与基线

- 仓库 https://github.com/skyyzc/Compositor-ZH；GitHub 及 CLI 账号 skyyzc。
- 当前官方源配置 upstream.json：1.5.5，提交 b31ea029762ecb782699df971e1412168602a44d；最近已发布汉化为 1.5.5 preview.1。
- 原安装 /Applications/Compositor.app 未修改；独立预览 Bundle ID local.compositor.zh。
- 本机无需 Xcode。GitHub macos-26 / Xcode 26.6 / Python 3.12 构建。
- translations/zh-Hans.tsv 是独立词库；scripts/prepare.py + adapt.py 生成 build-source。
- Document 模型文件保持字节不变（回归验证）。混合模式菜单用 representedObject 保存原始标识，显示译名独立。
- 官方更新器已停用；更新菜单链接项目 Actions。尚未实现自动安装及回退。
- 临时签名，无 Developer ID 签名或 Apple 公证。用户截图证实 Gatekeeper 拦截；已提供 Apple 官方手动确认步骤，不能宣称软件通过 Apple 安全认证。

## 人工截图 Ground Truth

1. 第一版菜单中文，但 Width/Height、画布类型、工具栏仍英文。
2. preview.2 截图确认宽度/高度、透明画布、像素、混合模式正常等显示中文，程序可打开。
3. preview.2 截图仍有 Last Filter、Progressive Blur、Bloom / Glow、Scanlines、Tonal Contrast、Camera Raw Filter、空图层提示、文字工具底部说明、Untitled 标签英文。
4. 左侧“格式”是 SF Symbol 的文字工具图标显示，不是形状工具标题；当前改为 T 图标，待截图验收。
5. 保存/加载、图像编辑、快捷键及导出未获得人工验收。

## 上一轮交付：1.5.3 preview.3

- 代码提交 830d6996b9c9b88ecb11d192f5dad5e3e29b8ca9。
- 补齐上述滤镜名称，接入上次滤镜菜单、空图层提示及所有工具的底部操作说明。
- 未保存标签显示“未命名”；已保存文件名保持原样。
- 词库 676 条；保守静态候选缺词 0，不代表完整 UI 覆盖率。
- 本地 4 项定向回归和相关 Swift 语法解析通过。
- 云端构建 https://github.com/skyyzc/Compositor-ZH/actions/runs/39537870102，结论 success；构建、4 项回归、打包通过。

## 已发布的上一版

preview.2：https://github.com/skyyzc/Compositor-ZH/releases/tag/v1.5.3-zh.preview.2
成功构建 https://github.com/skyyzc/Compositor-ZH/actions/runs/39537038012。

## 持续维护

automationId=compositor，ACTIVE；每天上海时间 10:00 回到此聊天检查官方正式发行版，无变化保持安静，有新版继续翻译/回归/云端构建，仅在新产物、实质失败或用户操作必需时通知。禁止桌面操作。涉及本地文件时需电脑及 Codex 保持运行。未验收版本只发布预览。

## NEXT

1.5.5 preview.1 已云端校验发布，待用户截图验收；随后按截图继续适配其余界面。保留验证边界，不把词库规模或构建通过当作完整目标已完成。

## preview.3 已交付

https://github.com/skyyzc/Compositor-ZH/releases/tag/v1.5.3-zh.preview.3
ZIP SHA256 aefd8ff27ab1604229b464ccea7c034f4c327bf45a49a1436ce3890db5dad752，与下载产物和 Release digest 一致，asset uploaded。本轮无桌面/应用操作。修复实现和构建验证完成，视觉结果待用户截图。

## 持续维护 2026-10-22：官方 1.5.5

- 检出官方 v1.5.5（发布于 2026-10-21 22:09:13 UTC）；固定源 b31ea029762ecb782699df971e1412168602a44d。
- 新增 RGB 分离、通道打包、字体搜索、线型和压感相关译文；总计 706 条，静态候选缺词 0。
- 回归发现上游将空图层说明 image 改为 file 导致精确替换失效，已定向修复；5 项本地化边界回归通过。
- 修正生成项目的产品名替换范围：仅 app 两个配置更名，保留测试 target 名称；固定 app module Compositor 并更新 TEST_HOST，使上游单元测试可针对中文版构建。
- 上游格式从 14 升至 16；不修改或降级其模型逻辑。新版保存的 v16 项目不能用旧版读取，预览说明必须提醒使用副本。
- 代码提交 1ec600b07fd0df15eda5efac2bf4564704133e35，云端构建 https://github.com/skyyzc/Compositor-ZH/actions/runs/39709639138，结论 success；5 项本地化边界回归及 44 项相关上游单元测试通过。
- 不操作用户桌面、不启动/安装本机应用。原版和已发布 1.5.3 预览保持不变；UI 仍须人工截图验收。

## 当前交付：1.5.5 preview.1（2026-10-22）

- https://github.com/skyyzc/Compositor-ZH/releases/tag/v1.5.5-zh.preview.1
- ZIP：https://github.com/skyyzc/Compositor-ZH/releases/download/v1.5.5-zh.preview.1/Compositor-ZH-1.5.5-preview.1.zip
- Release asset uploaded，19,186,912 字节；SHA256 6b27fb2b0fb637df826918f7a88cf450900a4c3a843ac8ef82db9b2c8b91a6f9。
- 发布流程 https://github.com/skyyzc/Compositor-ZH/actions/runs/39711636697 success：校验原始构建 ZIP、检查 app 版本/标识、清理测试附带的 .xctest、重新临时签名并验证、打包上传 Release。
- 本机 GitHub 产物下载多次 TLS 超时，已改为纯云端校验发布；没有为此更改网络/安全设置。
- 初版云端 Release 创建遭 GITHUB_TOKEN 403；改用用户已授权 CLI 创建 tag/Release 记录，再由云端上传资产，已验证可行。未来发布：先确认代码 build run success；使用 gh 用户连接创建准确 SHA 的 tag 和预览 Release；将 release-notes.md 更新为本次说明；运行 publish.yml 输入 run_id 和 tag。不要把用户令牌上传为仓库秘密。
- .github/workflows/build.yml 的上游测试改用 build-regression 派生目录，避免未来混入分发 app；发布脚本仍清理 .xctest 并验签。UI 和实机压感体验未验收，整体 PARTIAL。
- 未跟踪的 default.profraw 为旧会话遗留，不属于汉化源码，未改动或提交。
