from asyncio import gather, run

from aiogt import Translaitor


async def main():
    t = Translaitor()

    texts = ["hello world", "hello russia", "hello russia", "good morning"]

    translations = await gather(
        *[t.translate(txt, target="ru", source="en") for txt in texts]
    )

    print(translations)

    await t.transport.close()


run(main())
