from abc import ABC, abstractmethod
from typing import Optional


class Storage(ABC):
    @abstractmethod
    async def get(self, key: int) -> Optional[str]:
        raise ...

    @abstractmethod
    async def set(self, key: int, value: str) -> bool:
        raise ...
