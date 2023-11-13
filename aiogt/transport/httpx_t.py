import html

from urlcon import Constructor

from .base import Transport

try:
    import httpx
except ImportError:
    pass


class HttpxTransport(Transport):
    def __init__(self):
        self.conn = httpx.AsyncClient()

    async def send(self, target_lang: str, source_lang: str, text: str) -> str:
        url = Constructor("translate.google.com") / "m"

        response = await self.conn.get(
            str(url),
            params={"tl": target_lang, "sl": source_lang, "q": text},
        )

        return html.unescape(response.text)


    async def close(self):
        await self.conn.aclose()