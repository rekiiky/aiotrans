from aiogt import Translaitor
from asyncio import run

async def main():
    t = Translaitor()
    print(await t.translate("Hello"))

    await t.transport.close()

run(main())
