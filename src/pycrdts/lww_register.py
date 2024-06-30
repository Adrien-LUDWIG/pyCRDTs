from typing import Self
from typing import TypeVar

from pycrdts.utils.timestamp import Timestamp

T = TypeVar("T")


class LWWRegister:
    def __init__(self, id: int):
        self.id: int = id
        self.x: T = None
        self.timestamp = Timestamp(id)

    def assign(self, value: T) -> None:
        self.x = value
        self.timestamp.tick(self.id)

    def value(self) -> T:
        return self.x

    def compare(self, other: Self) -> bool:
        return self.timestamp.compare(other.timestamp)

    def merge(self, other: Self) -> None:
        if self.compare(other):
            self.x = other.x
            self.timestamp.merge(other.timestamp)

    def __str__(self) -> str:
        return f"(Value: {self.x}, Timestamp: {self.timestamp})"
