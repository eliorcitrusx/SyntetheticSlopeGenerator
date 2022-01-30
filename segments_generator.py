import numpy as np
from typing import List
from segment import Segment
from type import Type


class SegmentsGenerator:
    def __init__(self, d: int, b_low: List, b_high: List):
        x_low = [[] for _ in range(d)]
        x_high = [[] for _ in range(d)]
        for i in range(d):
            x_low[i] = range(b_low[i], b_high[i] - 1, 1)
            x_high[i] = range(b_low[i] + 1, b_high[i], 1)
            print(i)
        grid_low_edge = np.meshgrid(*x_low)
        grid_high_edge = np.meshgrid(*x_high)
        segment_vec = np.vectorize(Segment)
        segments = segment_vec(d, x_low, x_high)
        return segments


p = SegmentsGenerator(2, np.array([2, 2]), np.array([4, 4]))

print(p)
