from .storage.base import Storage


def hash_args(args, kwargs) -> int:
    return hash(args[1] + str(kwargs.get("target")) + str(kwargs.get("source")))


def simple_cache(cache: Storage):
    def __cache(func):
        async def wrapper(*args, **kwargs):
            result = await cache.get(hash_args(args, kwargs))

            if not result:
                result = await func(*args, **kwargs)
                await cache.set(hash_args(args, kwargs), result)

            return result

        return wrapper

    return __cache
