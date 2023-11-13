from typing import Optional

from .base import Storage


class MemoryStorage(Storage):
    def __init__(self, max_size: int = 100) -> None:
        self.storage = dict()
        self.max_size = max_size

    async def get(self, key: int) -> Optional[int]:
        return self.storage.get(key)

    async def set(self, key: int, value: str) -> bool:
        if len(self.storage) == self.max_size:
            self.storage.pop(next(iter(self.storage)))

        self.storage[key] = value

        return True
