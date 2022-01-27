from random import random, randint
import numpy as np
from sys import maxsize


class Segment:
    def __init__(self, d: int, b_low: np.ndarray, b_high: np.ndarray, m_low: int, m_high: int):
        self._d = d
        self._b_low = b_low
        self._b_high = b_high
        self._coef_A = np.random.rand(d) * randint(1, maxsize)
        self._coef_b = random() * randint(1, maxsize)
        self._m = randint(m_low, m_high)

    def generate_samples(self):
        x_samples = np.random.rand(self._m, self._d)
        y_samples = np.dot(x_samples, self._coef_A) + self._coef_b
        return np.column_stack((x_samples, y_samples))

    def get_data(self):
        ranges = {"ranges": {f"x{i + 1}": [self._b_low[i], self._b_high[i]] for i in range(self._d)}}
        coefficients = {"coefficients": {f"x{i + 1}": self._coef_A[i] for i in range(self._d)}}
        return [ranges, coefficients]

    def get_y(self, point):
        for i in range(self._d):
            if point[i] < self._b_low[i] or self._b_high[i] < point[i]:
                return None
        return np.dot(point, self._coef_A) + self._coef_b
