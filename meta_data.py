from dataclasses import dataclass
from typing import List
from type import Type
from segment import Segment


@dataclass
class MetaData:
    _d: int
    _segments: List[Segment]
    _type: Type
    _noise: int = 0

    @property
    def d(self):
        return self._d

    @property
    def segments(self):
        return self._segments
