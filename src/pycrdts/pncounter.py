from typing import Self

from .gcounter import GCounter


class PNCounter:
    def __init__(self, replicas_count: int, id: int):
        self.positive_counter: GCounter = GCounter(replicas_count, id)
        self.negative_counter: GCounter = GCounter(replicas_count, id)
        self.replicas_count: int = replicas_count
        self.id: int = id

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
