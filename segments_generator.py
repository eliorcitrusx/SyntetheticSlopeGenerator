import numpy as np
from typing import List
from segment import Segment
import itertools
from type import Type


class SegmentsGenerator:
    def __init__(self, d: int, b_low: List, b_high: List):
        x_low = [[] for _ in range(d)]
        x_high = [[] for _ in range(d)]
        for i in range(d):
            x_low[i] = np.arange(b_low[i], b_high[i] - 1, 1)
            x_high[i] = np.arange(b_low[i] + 1, b_high[i], 1)
            print(i)
        grid_low_edge = np.meshgrid(*x_low)
        grid_high_edge = np.meshgrid(*x_high)
        segment_vec = np.vectorize(Segment)
        low_edges = []
        high_edges = []
        counter = 0
        for low_edge in itertools.product(*x_low):
            low_edges.append(low_edge)
            counter += 1
        counter = 0
        for high_edge in itertools.product(*x_high):
            counter += 1
            high_edges.append(high_edge)
        for i in range (len(low_edges)):
            print(low_edges[i], high_edges[i])
        segments=[]
        for index in range(len(low_edges)):
            segments.append(Segment(d, low_edge, high_edge))
        self._segments = segments
    @property
    def segments(self):
        return self._segments


segments = SegmentsGenerator(2, np.array([2, 5]), np.array([8, 9]))
p = segments.get_segments()

print(p[0])
print(p[0].get_data())

#print(p[0])