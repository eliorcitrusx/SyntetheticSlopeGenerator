from dataclasses import dataclass
from typing import List, Optional
from data_type import DataType
from segment import Segment


@dataclass
class MetaData:
    _dimensions: int
    _segments: List[Segment]
    _data_type: DataType = DataType.CONTINUOUS
    _noise_level: int = 0

    @property
    def dimensions(self):
        return self._dimensions

    @property
    def segments(self):
        return self._segments

    def get_y_value(self, point: List) -> Optional[float]:
        if len(point) != self._dimensions:
            raise ValueError("A point must have the same dimensions as its dimensions")
        for segment in self._segments:
            y = segment.get_y_value(point)
            if y:
                return y
        return None
