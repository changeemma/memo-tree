from __future__ import annotations

from abc import ABC, abstractmethod


class ArchiveBase(ABC):
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return self.name

    def is_named(self, name: str) -> bool:
        return self.name == name

    @abstractmethod
    def browse(self, name) -> ArchiveBase:
        pass

    @abstractmethod
    def open(self) -> None:
        pass
