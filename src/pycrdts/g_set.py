from typing import Self


class GSet:
    def __init__(self):
        self.payload: set = set()

    def add(self, element: int) -> None:
        self.payload.add(element)

    def lookup(self, element: int) -> bool:
        return element in self.payload

    def compare(self, other: Self) -> bool:
        return self.payload.issubset(other.payload)

    def merge(self, other: Self) -> None:
        self.payload = self.payload.union(other.payload)

    def __str__(self) -> str:
        return str(self.payload)
