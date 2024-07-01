from typing import Optional
from typing import Self
from uuid import uuid4

from .g_counter import GCounter


class PNCounter:
    def __init__(self, id: Optional[uuid4] = None):
        self.id: uuid4 = uuid4() if id is None else id
        self.positive_counter: GCounter = GCounter(self.id)
        self.negative_counter: GCounter = GCounter(self.id)

    def increment(self) -> None:
        self.positive_counter.increment()

    def decrement(self) -> None:
        self.negative_counter.increment()

    def value(self) -> int:
        return self.positive_counter.value() - self.negative_counter.value()

    def compare(self, other: Self) -> bool:
        compare_positive = self.positive_counter.compare(other.positive_counter)
        compare_negative = self.negative_counter.compare(other.negative_counter)
        return compare_positive and compare_negative

    def merge(self, other: Self) -> None:
        self.positive_counter.merge(other.positive_counter)
        self.negative_counter.merge(other.negative_counter)

    def __str__(self) -> str:
        return f"Positive: {self.positive_counter}, Negative: {self.negative_counter}"
