# douparse.py · 抖解 DouParse 的 Python 客户端

单文件、零配置的 [视频解析](https://www.qiaiwan.top) API 客户端：粘贴分享链接，拿到无水印视频直链、图集直链、抖音原声 MP3 直链。核心就几十行，只依赖 `requests`，直接把 `douparse.py` 拷进你的项目即可。

- 主站：<https://www.qiaiwan.top>
- API 文档：<https://www.qiaiwan.top/api-docs>
- 在 AI 客户端里用（MCP）：<https://www.qiaiwan.top/ai>

## 快速开始

1. [注册账号](https://www.qiaiwan.top/account)自动领取 API Key（`dpk_` 开头，注册即送免费试用次数）；
2. 安装依赖：`pip install requests`；
3. 跑通第一个解析：

```python
from douparse import DouParse

dp = DouParse("dpk_xxxxxxxx")  # 或设环境变量 DOUPARSE_API_KEY
data = dp.parse("https://v.douyin.com/xxxxxx/")

# 视频类：无水印直链，自己下载，不经中转
if data["aweme_type"] == "video":
    dp.download("https://v.douyin.com/xxxxxx/", "video.mp4")

# 抖音原声 MP3：同一次响应里直接拿，无需第二个接口
mp3 = (data.get("music") or {}).get("play_url", "")
if mp3:
    dp.download_music("https://v.douyin.com/xxxxxx/", "bgm.mp3")
```

## 响应字段速查（按 `aweme_type` 分支处理）

| 字段 | 说明 |
| --- | --- |
| `aweme_type` | `video`（视频）/ `image`（图集）/ `product`（商品混合素材），**先按它分支** |
| `play_url` | 视频直链；图集为第一段动态视频；无视频商品为空字符串 |
| `images` | 图集图片直链列表（商品类 = 主图 + 详情图） |
| `music.play_url` | **抖音原声 MP3 直链**，拿到即可直接下载；非抖音平台 / 版权受限时为空字符串 |
| `music.play_url_backup` | 同一原声的备用 MP3 直链，主链失败时改用 |
| `cover` / `desc` / `author` | 封面、文案、作者 |
| `qualities` | 可选清晰度档位（多档位平台） |
| `product` | 商品类专用：`videos[]` / `main_images` / `detail_images` / `shop_name` |

下载提示：直链有时效（通常数小时），过期重新解析即可（缓存期内不扣次数）；部分平台 CDN 校验 `Referer`，下载时带上对应平台域名即可。

## 错误码速查

| code | 含义 | 处理 |
| --- | --- | --- |
| `0` | 成功 | — |
| `1001` | 解析失败 | 作品删除/私密/链接无效（`fail_side:"link"`，扣 1 次）；平台变动不扣 |
| `1002` | 网络错误 | 不扣次数，重试 |
| `1401` | Key 无效或停用 | 检查 `Authorization` 头，重新领取 |
| `1402` | 次数用完 | 到[个人中心](https://www.qiaiwan.top/account)充值 |
| `1429` | 触发限频 | 默认 10 次/分钟，降低并发 |
| `1500` / `1503` | 服务异常 / 维护 | 不扣次数，稍后重试 |

计费规则（对外承诺）：**缓存命中、出口风控、网络错误、服务异常一律不扣次数**；真实解析成功扣 1 次。完整[定价与成本测算](https://www.qiaiwan.top/api-pricing)。

## 在 AI 客户端里用（MCP）

不写代码也可以：本站提供 MCP Server（工具：`parse_video` / `get_balance` / `redeem_code`），已收录到[官方 Registry](https://mcptry.com/servers/top.qiaiwan.www/douparse)。在 Claude Desktop、Cursor 等客户端里加一段配置，直接对 AI 说「帮我解析这条抖音链接」即可。一键安装指引见 [AI 接入专页](https://www.qiaiwan.top/ai)。

## License

MIT。解析内容仅限个人学习使用，请勿用于侵权用途。
