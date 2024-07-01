from typing import Dict
from typing import Optional
from typing import Self
from uuid import uuid4


class GCounter:
    def __init__(self, id: Optional[uuid4] = None):
        self.payload: Dict[uuid4, int] = {}
        self.id: uuid4 = uuid4() if id is None else id

    def increment(self) -> None:
        if self.id not in self.payload:
            self.payload[self.id] = 0
        self.payload[self.id] += 1

    def value(self) -> int:
        return sum(self.payload.values())

    def compare(self, other: Self) -> bool:
        for id in self.payload:
            if id not in other.payload or self.payload[id] > other.payload[id]:
                return False
        return True

    def merge(self, other: Self) -> None:
        for id in other.payload:
            self.payload[id] = max(self.payload.get(id, 0), other.payload[id])

    def __str__(self) -> str:
        return str(self.payload)
