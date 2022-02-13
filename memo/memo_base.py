from __future__ import annotations

from abc import ABC, abstractmethod


class MemoBase(ABC):
    def __init__(self, name: str):
        self.name = name

    def print(self) -> str:
        return self.name

    def is_named(self, name: str) -> bool:
        return self.name == name

    @abstractmethod
    def has_node(self, name: str) -> bool:
        pass

    @abstractmethod
    def browse(self, name) -> MemoBase:
        pass

    @abstractmethod
    def open(self) -> None:
        pass
