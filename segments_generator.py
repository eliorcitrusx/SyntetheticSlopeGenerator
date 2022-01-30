import numpy as np
from typing import List
from segment import Segment
import itertools
from type import Type


class SegmentsGenerator:
    def __init__(self, d: int, b_low: List, b_high: List):
        x_low = [np.arange(b_low[i], b_high[i] - 1, 1) for i in range(d)]
        x_high = [np.arange(b_low[i] + 1, b_high[i], 1) for i in range(d)]
        low_edges = []
        high_edges = []
        for low_edge in itertools.product(*x_low):
            low_edges.append(low_edge)
        for high_edge in itertools.product(*x_high):
            high_edges.append(high_edge)
        segments_list = []
        for i in range(len(low_edges)):
            segments_list.append(Segment(d, low_edges[i], high_edges[i]))
        self._segments = segments_list

    @property
    def segments(self):
        return self._segments

#
# segments = SegmentsGenerator(2, np.array([2, 5]), np.array([8, 9]))
# print(type(segments))
# p = segments.segments
#
# print(type(p))
#
# for segment in p:
#     print(segment.get_data())