from itertools import product
from typing import List
import numpy as np
from segment import Segment


class SegmentsGenerator:
    def __init__(self, dimensions: int, boundaries_low: List, boundaries_high: List):
        self._segments = self.generate_segments(dimensions, boundaries_low, boundaries_high)

    @property
    def segments(self):
        return self._segments

    @staticmethod
    def generate_segments(dimensions: int, boundaries_low: List, boundaries_high: List) -> List[Segment]:
        x_boundaries_low = [np.arange(boundaries_low[i], boundaries_high[i] - 1, 1) for i in range(dimensions)]
        x_boundaries_high = [np.arange(boundaries_low[i] + 1, boundaries_high[i], 1) for i in range(dimensions)]
        low_edges = [low_edge for low_edge in product(*x_boundaries_low)]
        high_edges = [high_edge for high_edge in product(*x_boundaries_high)]
        return [Segment(dimensions, low_edges[i], high_edges[i]) for i in range(len(low_edges))]
