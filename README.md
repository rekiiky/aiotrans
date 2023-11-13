# Simple async Google Translate library

#### Instalation:
```pip install aiogt[aiohttp]``` or ```pip install aiogt[httpx]```

#### Featrures
* Fast and reliable - it uses the same servers that translate.google.com uses
* Support for httpx and aiohttp
* Fully asyncio support
* Simple result caching

#### Example
```python
from asyncio import run

from aiogt import Translaitor


async def main():
    t = Translaitor()
    print(await t.translate("Hello", target='ru', source='en'))

    await t.transport.close()

run(main())
```