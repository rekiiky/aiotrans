from abc import ABC, abstractmethod


class Transport(ABC):
    @abstractmethod
    def __init__(self):
        raise ...

    @abstractmethod
    async def send(self, target_lang: str, source_lang: str, text: str) -> str:
        raise ...

    @abstractmethod
    async def close(self):
        raise ...
