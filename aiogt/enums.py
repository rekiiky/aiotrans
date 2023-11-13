from enum import Enum

from aiogt.transport import AiohttpTransport, HttpxTransport


class Transport(Enum):
    aiohttp = AiohttpTransport
    httpx = HttpxTransport
