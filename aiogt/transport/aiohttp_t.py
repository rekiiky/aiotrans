import html

from urlcon import Constructor

from .base import Transport

try:
    import aiohttp
except ImportError:
    pass


class AiohttpTransport(Transport):
    def __init__(self):
        self.conn = aiohttp.ClientSession()

    async def send(self, target_lang: str, source_lang: str, text: str) -> str:
        url = Constructor("translate.google.com") / "m"

        response = await self.conn.get(
            str(url),
            params={"tl": target_lang, "sl": source_lang, "q": text},
        )

        return html.unescape(await response.text(encoding="utf-8"))

    async def close(self):
        await self.conn.close()