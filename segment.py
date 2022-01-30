from typing import List, Optional
from random import random, randint
from sys import maxsize
import numpy as np


class Segment:
    def __init__(self, dimensions: int, boundaries_low: np.ndarray, boundaries_high: np.ndarray,
                 coefficients_A: np.ndarray = None, coefficients_B: float = None, data_samples_number: int = None):
        self._dimensions = dimensions
        self._boundaries_low = boundaries_low
        self._boundaries_high = boundaries_high
        self._coefficients_A = coefficients_A if coefficients_A else np.random.rand(dimensions) * randint(1, maxsize)
        self._coefficients_B = coefficients_B if coefficients_B else random() * randint(1, maxsize)
        self._data_samples_number = data_samples_number if data_samples_number else randint(1, 2 * dimensions)

    def generate_data_samples(self) -> np.ndarray:
        x_samples = np.random.rand(self._data_samples_number, self._dimensions)
        y_samples = np.dot(x_samples, self._coefficients_A) + self._coefficients_B
        return np.column_stack((x_samples, y_samples))

    def export_to_json(self):
        ranges = {f"x{i + 1}": [self._boundaries_low[i], self._boundaries_high[i]] for i in range(self._dimensions)}
        coefficients_A = {f"x{i + 1}": self._coefficients_A[i] for i in range(self._dimensions)}
        return {"ranges": ranges, "coefficients_A": coefficients_A, "coefficients_B": self._coefficients_B,
                "data_samples_number": self._data_samples_number}

    def get_y_value(self, point: List) -> Optional[float]:
        for i in range(self._dimensions):
            if point[i] < self._boundaries_low[i] or self._boundaries_high[i] < point[i]:
                return None
        return np.dot(point, self._coefficients_A) + self._coefficients_B
