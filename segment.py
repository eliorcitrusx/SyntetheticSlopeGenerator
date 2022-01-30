from random import random, randint
import numpy as np
from sys import maxsize
from typing import List


class Segment:
    def __init__(self, d: int, b_low: np.ndarray, b_high: np.ndarray, coef_A: np.ndarray = None, coef_B: float = None,
                 m: int = None):
        self._d = d
        self._b_low = b_low
        self._b_high = b_high
        self._coef_A = coef_A if coef_A else np.random.rand(d) * randint(1, maxsize)
        self._coef_B = coef_B if coef_B else random() * randint(1, maxsize)
        self._m = m if m else randint(1, 2 * self._d)

    def generate_samples(self):
        x_samples = np.random.rand(self._m, self._d)
        y_samples = np.dot(x_samples, self._coef_A) + self._coef_B
        return np.column_stack((x_samples, y_samples))

    def get_data(self):
        ranges = {f"x{i + 1}": [self._b_low[i], self._b_high[i]] for i in range(self._d)}
        coefficients = {f"x{i + 1}": [self._coef_A[i], self._coef_B] for i in range(self._d)}
        return {"ranges": ranges, "coefficients": coefficients, "m": self._m}

    def get_y(self, point: List):
        for i in range(self._d):
            if point[i] < self._b_low[i] or self._b_high[i] < point[i]:
                return None
        return np.dot(point, self._coef_A) + self._coef_B
