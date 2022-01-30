import numpy as np
from typing import List
from segment import Segment
import itertools


class SegmentsGenerator:
    def __init__(self, d: int, b_low: List, b_high: List):
        self._segments = self.generate_segments(d, b_low, b_high)

    @property
    def segments(self):
        return self._segments

    @staticmethod
    def generate_segments(d: int, b_low: List, b_high: List) -> List[Segment]:
        x_low = [np.arange(b_low[i], b_high[i] - 1, 1) for i in range(d)]
        x_high = [np.arange(b_low[i] + 1, b_high[i], 1) for i in range(d)]
        low_edges = [low_edge for low_edge in itertools.product(*x_low)]
        high_edges = [high_edge for high_edge in itertools.product(*x_high)]
        return [Segment(d, low_edges[i], high_edges[i]) for i in range(len(low_edges))]
