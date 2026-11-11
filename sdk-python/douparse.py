"""抖解 DouParse 开放 API 的极简 Python 客户端（单文件，仅依赖 requests）。

文档：https://www.qiaiwan.top/api-docs
领 Key：https://www.qiaiwan.top/account （注册账号自动领取）

快速上手：

    from douparse import DouParse

    dp = DouParse("dpk_xxxxxxxx")            # 或设环境变量 DOUPARSE_API_KEY
    data = dp.parse("https://v.douyin.com/xxxxxx/")

    if data["aweme_type"] == "video":
        print(data["play_url"])              # 无水印视频直链
    mp3 = (data.get("music") or {}).get("play_url", "")
    print(mp3)                               # 抖音原声 MP3 直链（可能为空）

如实说明（免得踩坑）：
    - 支持抖音、快手、小红书、B站、视频号等 10+ 平台，抖音字段最全；
      非抖音平台 / 版权受限 / 上游风控时 music.play_url 是空字符串
      （上游无独立音频），需要音频请下载视频后自行抽轨。
    - 直链有时效（通常数小时），过期重新解析即可；同一链接缓存期内不扣次数。
    - 默认限频 10 次/分钟（1429 = 触发限频）；缓存命中、我方失败不扣次数，
      链接本身不可用（作品删除/私密，fail_side="link"）扣 1 次。
    - 解析内容仅限个人学习使用，请勿用于侵权用途。
"""

import os

import requests

DEFAULT_BASE = "https://www.qiaiwan.top"


class DouParseError(Exception):
    """API 返回非 0 code 或请求本身失败时抛出。

    属性：
        code: 接口错误码（网络错误时为 None）
        fail_side: "link" 表示链接本身不可用（会扣次数）；其余为平台侧失败
    """

    def __init__(self, message, code=None, fail_side=None):
        super().__init__(message)
        self.code = code
        self.fail_side = fail_side


class DouParse:
    """用法：DouParse("dpk_xxx").parse(url) -> data 字典。"""

    def __init__(self, api_key=None, base_url=None, timeout=30):
        self.api_key = api_key or os.environ.get("DOUPARSE_API_KEY", "")
        self.base_url = (base_url or DEFAULT_BASE).rstrip("/")
        self.timeout = timeout
        self.last_remaining = None  # 上次调用后的剩余次数
        self.last_cost = None       # 上次调用扣减的次数

    def _headers(self):
        if not self.api_key:
            raise DouParseError("缺少 API Key：构造时传入，或设置环境变量 DOUPARSE_API_KEY")
        return {"Authorization": "Bearer " + self.api_key}

    def _request(self, method, path, **kwargs):
        r = requests.request(method, self.base_url + path,
                             headers=self._headers(), timeout=self.timeout, **kwargs)
        try:
            body = r.json()
        except ValueError:
            raise DouParseError("HTTP %s：非 JSON 响应" % r.status_code)
        self.last_remaining = body.get("remaining")
        self.last_cost = body.get("cost")
        if body.get("code") not in (0, None):
            raise DouParseError(
                "code=%s %s" % (body.get("code"), body.get("message") or "解析失败"),
                code=body.get("code"),
                fail_side=body.get("fail_side"),
            )
        return body

    def parse(self, url):
        """解析一条分享文本 / 短链 / 完整链接，返回 data 字典。

        常用字段：play_url（视频直链）、images（图集列表）、
        music.play_url / play_url_backup（抖音原声 MP3）、
        cover / desc / author、qualities（可选清晰度）、
        aweme_type（"video" | "image" | "product"，请按此分支处理）。
        商品类请读 data["product"]（含 videos / main_images / detail_images），
        不能只下载 play_url。
        """
        body = self._request("POST", "/api/v1/parse", json={"url": url})
        data = body.get("data")
        if data is None:
            raise DouParseError("响应缺少 data 字段：%s" % str(body)[:200])
        return data

    def balance(self):
        """查询 Key 状态，返回整个响应体。

        常用字段：balance（剩余次数，与网页端共享池通用）、
        rpm（每分钟限频）、today_used（今日已用）。
        """
        return self._request("GET", "/api/v1/balance")

    @staticmethod
    def _download(url, path, referer=None):
        headers = {"Referer": referer} if referer else {}
        with requests.get(url, headers=headers, stream=True, timeout=60) as r:
            r.raise_for_status()
            with open(path, "wb") as f:
                for chunk in r.iter_content(8192):
                    f.write(chunk)

    def download(self, url, path, referer=None):
        """解析并把无水印视频保存到 path，返回 data 字典。

        部分平台 CDN 校验 Referer，下载失败时按平台域名传 referer，
        例如抖音动态图用 "https://www.douyin.com/"。
        """
        data = self.parse(url)
        play = data.get("play_url")
        if not play:
            raise DouParseError("play_url 为空：图集请读 images，商品请读 product.videos")
        self._download(play, path, referer)
        return data

    def download_music(self, url, path):
        """解析并把抖音原声 MP3 保存到 path，返回 data 字典。

        主链失败自动改用 play_url_backup；非抖音平台 / 版权受限时
        music.play_url 为空字符串，此时抛 DouParseError（不猜测、不伪造）。
        """
        data = self.parse(url)
        music = data.get("music") or {}
        mp3 = music.get("play_url") or music.get("play_url_backup")
        if not mp3:
            raise DouParseError("该作品没有可用的原声直链（非抖音平台或版权受限）")
        self._download(mp3, path)
        return data
