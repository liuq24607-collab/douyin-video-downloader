# 抖解 DouParse · 抖音/小红书/快手/B站/视频号 视频无水印解析下载工具

[![mcptry](https://mcptry.com/badge/top.qiaiwan.www/douparse)](https://mcptry.com/servers/top.qiaiwan.www/douparse)

>  在线使用：**<https://www.qiaiwan.top>** —— 每天 3 次免费额度 · 会员不限量 · 手机电脑通用
>
> DouParse（抖解）：短视频无水印解析与下载在线工具，粘贴分享链接即可提取无水印原始视频。

粘贴各平台分享链接，一键解析并**无水印下载**原始视频、图集、背景音乐 MP3 与封面。
支持 **抖音、小红书、B站（哔哩哔哩）、快手、微信视频号、知乎、好看视频、西瓜视频、贴吧** 九大平台，
并提供**免费开放 API**（视频解析接口）与 **MCP Server**，适合脚本自动化与 AI 助手调用。

[🌐 在线网站](https://www.qiaiwan.top) · [🔌 开放 API 文档](https://www.qiaiwan.top/api-docs) · [🤖 MCP 接入](#-mcp-serverai-助手直接调用) · [🧩 浏览器扩展](https://www.qiaiwan.top/extension) · [📖 抖音无水印下载教程](https://www.qiaiwan.top/how-to-download-douyin-video)

> 💰 **获取完整源码 / 商业授权**：本仓库仅为功能演示与推广，**不包含服务端源代码**。
> 如需购买完整源码（九大平台解析引擎 + 网页前端 + 浏览器扩展 + 开放 API + 部署搭建），
> 或洽谈商业授权 / 定制 / 私有化部署，请加微信 **`Liu782694171`**（备注「源码」）。

![DouParse 首页](assets/promo-img-home.png)

## ✨ 功能特性

- 🎵 **抖音去水印**：抖音视频无水印下载、图集逐张/批量下载、实况 Live 图、背景音乐 MP3 提取、封面下载、文案复制
- 📕 **小红书去水印**：小红书视频/图片/图集/实况 Live 图无水印保存，xhslink 短链直接解析
- ⚡ **快手去水印**：快手短视频无水印下载，v.kuaishou.com 分享链接粘贴即解
- 📺 **B站视频下载**：b23.tv 短链 / BV 号解析，高清下载、封面提取、音频 MP3 提取
- 💬 **视频号下载**：微信视频号视频无水印解析保存
- 💡 **知乎 / 👀 好看视频 / 🍉 西瓜视频 / 🎪 贴吧**：视频无水印解析下载
- 🧰 **Pro 工具箱**：创作者批量提取、作品数据等高级功能
- 🔌 **开放 API**：一个接口解析 10+ 平台返回无水印直链，免费领 Key，缓存命中不扣次数
- 🤖 **MCP Server**：已发布至官方 MCP Registry，AI 助手可直接调用解析工具
- 🆓 每天 3 次免费额度、不装 App、网页版在线使用，不存储任何视频文件

## 🚀 使用方法（三步）

1. 在抖音 / 小红书 / 快手 / B站 / 视频号等 App 内点「分享」→「复制链接」；
2. 打开 <https://www.qiaiwan.top>，把整段分享文本粘贴进输入框；
3. 点「开始解析」，下载无水印视频 / 图集 / 音乐 / 封面。

支持批量解析：一次粘贴多个链接自动排队逐条解析。

## 📚 图文教程

| 教程 | 链接 |
|---|---|
| 抖音无水印下载教程 | <https://www.qiaiwan.top/how-to-download-douyin-video> |
| 抖音图集批量打包下载 | <https://www.qiaiwan.top/how-to-batch-download-douyin-images> |
| 抖音背景音乐提取 | <https://www.qiaiwan.top/how-to-extract-douyin-music> |
| 抖音 4K 高清下载 | <https://www.qiaiwan.top/how-to-download-douyin-hd-video> |
| iPhone / 安卓保存抖音无水印 | <https://www.qiaiwan.top/how-to-save-douyin-video-on-iphone> |
| 小红书无水印下载教程 | <https://www.qiaiwan.top/how-to-download-xiaohongshu-video> |
| 快手无水印下载教程 | <https://www.qiaiwan.top/how-to-download-kuaishou-video> |
| B站视频下载教程 | <https://www.qiaiwan.top/how-to-download-bilibili-video> |
| 视频号视频下载教程 | <https://www.qiaiwan.top/shipinhao-shipin-xiazai> |
| 在线视频去水印 | <https://www.qiaiwan.top/online-video-watermark-remover> |

更多教程与「抖音去水印 / 抖音解析 / 小红书去水印工具 / 快手去水印在线 / B站视频下载工具 /
视频去水印免费网站 / 短视频去水印工具 / 视频解析下载 / 保存到手机相册」等场景，见网站首页与帮助。

## 🔌 开放 API（开发者）

一个接口解析抖音、快手、小红书、B站、视频号等 10+ 平台，返回无水印直链：

```bash
curl -X POST "https://www.qiaiwan.top/api/v1/parse" \
  -H "Authorization: Bearer dpk_xxxxxxxx" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://v.douyin.com/xxxxxx/"}'
```

免费领取 API Key、配额计费规则与错误码见 [开放 API 文档](https://www.qiaiwan.top/api-docs)。

## 🤖 MCP Server（AI 助手直接调用）

DouParse 已发布到 [官方 MCP Registry](https://registry.modelcontextprotocol.io/)（`top.qiaiwan.www/douparse`），
Cursor / Claude Desktop / VS Code 等 MCP 客户端可直接接入解析能力，无需自行封装 HTTP 接口。

完整接入指引（一键安装到 Cursor / VS Code、工具说明、常见问题、英文摘要）：[AI 接入专页](https://www.qiaiwan.top/ai)；
供 AI 助手核对功能、额度与接口的事实说明：[llms.txt](https://www.qiaiwan.top/llms.txt)。

| 项 | 值 |
|---|---|
| 传输协议 | Streamable HTTP |
| 端点 | `https://www.qiaiwan.top/mcp/` |
| 鉴权 | 请求头 `Authorization: Bearer <API Key>`（在 [账号页](https://www.qiaiwan.top/account) 免费领取） |
| 官方清单 | 本仓库根目录 [`server.json`](server.json) |

客户端配置示例：

```json
{
  "mcpServers": {
    "douparse": {
      "url": "https://www.qiaiwan.top/mcp/",
      "headers": { "Authorization": "Bearer dpk_xxxxxxxx" }
    }
  }
}
```

可用工具：

| 工具 | 说明 | 参数 |
|---|---|---|
| `parse_video` | 解析分享链接或整段分享文本，返回无水印视频直链、图集图片、背景音乐与文案 | `url` |
| `get_balance` | 查询当前 Key 的剩余次数、每分钟限频与今日已用 | 无 |
| `redeem_code` | 用充值码给账号增加调用次数（一码一用） | `code` |

`parse_video` 仅在真实解析成功时扣 1 次，缓存命中与失败不扣。返回的无水印直链均为平台 CDN 地址，有时效，过期重新解析即可。

## ❓ FAQ

- **有免费额度吗？** 有，游客每天 3 次免费解析；需要更多次数可开通会员或领取 API 调用额度。
- **会保存我的视频吗？** 不会，服务器仅临时解析转发，不落地存储。
- **支持哪些链接？** 各平台分享短链、完整链接、整段带文案的分享文本均可自动识别。
- **私密/会员内容能下载吗？** 不能，仅支持公开可见作品。

## English

**DouParse – online watermark remover & downloader for short videos.**
Parse share links from Douyin (TikTok China), Xiaohongshu (RED), Kuaishou, Bilibili, WeChat Channels,
Zhihu and more; download original videos, image sets, background music and covers **without watermark**.
Free daily quota (3 parses), no app install, membership for unlimited use. A free **open API** and an
official-registry **MCP server** return watermark-free direct links for developers and AI assistants.
Try it online: <https://www.qiaiwan.top>

## 💰 源码购买 / 商业授权

本仓库（含在线站点）展示的是**成品功能与使用方式**，**不提供服务端源代码**。若你需要：

- **完整源码**：九大平台解析引擎（后端）+ 网页前端 + 浏览器扩展 + 开放 API 全套代码；
- **部署搭建**：帮你部署到自己的服务器 / 域名，可独立运营；
- **商业授权 / 定制**：二次开发、功能定制、私有化部署、品牌替换等。

请联系：

| 方式 | 号码 |
|---|---|
| 微信 | `Liu782694171`（添加时备注「源码」） |

> 源码采用一次性买断 / 授权制，具体价格与交付方式加微信详谈。

## 版权声明 / License

版权所有 © 2026 DouParse（抖解）· 保留所有权利（All Rights Reserved）。

本仓库的文档、图片与在线服务仅供展示与推广，**不包含服务端源代码**。未经版权所有人书面授权，
禁止复制、转载、修改、分发、再许可或用于任何商业用途。如需完整源码或商业授权，
请加微信 `Liu782694171` 联系（备注「源码」）。
