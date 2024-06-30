from typing import Self


class Timestamp:
    def __init__(self, id: int):
        self.clock = 0
        self.id = id

    def tick(self, id: int) -> None:
        self.clock += 1
        self.id = id

    def compare(self, other: Self) -> bool:
        return self.clock < other.clock or (
            self.clock == other.clock and self.id <= other.id
        )

    def merge(self, other: Self) -> None:
        if self.compare(other):
            self.clock = other.clock
            self.id = other.id

    def __str__(self) -> str:
        return f"(Clock: {self.clock}, Id: {self.id})"
