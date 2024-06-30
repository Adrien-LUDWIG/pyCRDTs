from typing import Self

from .g_set import GSet


class TwoPhaseSet:
    def __init__(self):
        self.add_set: GSet = GSet()
        self.remove_set: GSet = GSet()

    def add(self, element: int) -> None:
        self.add_set.add(element)

    def remove(self, element: int) -> None:
        if self.add_set.lookup(element):
            self.remove_set.add(element)

    def lookup(self, element: int) -> bool:
        is_in_add = self.add_set.lookup(element)
        is_not_in_remove = not self.remove_set.lookup(element)
        return is_in_add and is_not_in_remove

    def compare(self, other: Self) -> bool:
        is_add_subset = self.add_set.compare(other.add_set)
        is_remove_subset = self.remove_set.compare(other.remove_set)
        return is_add_subset and is_remove_subset

    def merge(self, other: Self) -> None:
        self.add_set.merge(other.add_set)
        self.remove_set.merge(other.remove_set)

    def __str__(self) -> str:
        return f"(Add: {self.add_set}, Remove: {self.remove_set})"
