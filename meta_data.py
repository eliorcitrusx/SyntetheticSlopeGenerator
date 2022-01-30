from dataclasses import dataclass
from typing import List
from type import Type
from segment import Segment


@dataclass
class MetaData:
    _d: int
    _segments: List[Segment]
    _type: Type = Type.CONTINUOUS
    _noise: int = 0

    @property
    def d(self):
        return self._d

    @property
    def segments(self):
        return self._segments

    def get_y(self, point: List):
        if len(point) != self._d:
            raise ValueError("A point must have the same dimensions as its dimensions")
        for segment in self._segments:
            y = segment.get_y(point)
            if y:
                return y
        return None
