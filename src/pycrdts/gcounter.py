from typing import Self


class GCounter:
    def __init__(self, replicas_count: int, id: int):
        self.payload: int = [0] * replicas_count
        self.replicas_count: int = replicas_count
        self.id: int = id

    def increment(self) -> None:
        self.payload[self.id] += 1

    def value(self) -> int:
        return sum(self.payload)

    def compare(self, other: Self) -> bool:
        return all(
            self.payload[i] <= other.payload[i]
            for i in range(self.replicas_count)
        )

    def merge(self, other: Self) -> None:
        for i in range(self.replicas_count):
            self.payload[i] = max(self.payload[i], other.payload[i])
