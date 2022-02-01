from typing import Optional, Dict, Any
from random import random, randint
from sys import maxsize
import numpy as np


class Segment:
    def __init__(self,
                 dimensions: int,
                 boundaries_low: np.ndarray,
                 boundaries_high: np.ndarray,
                 data_samples_min: int,
                 data_samples_max: int,
                 coefficients_A: np.ndarray = None,
                 coefficients_B: float = None,
                 data_samples_number: int = None):
        self._dimensions = dimensions
        self._boundaries_low = boundaries_low
        self._boundaries_high = boundaries_high
        self._data_samples_min = data_samples_min
        self._data_samples_max = data_samples_max
        self._coefficients_A = coefficients_A if coefficients_A else np.random.rand(dimensions) * randint(1, maxsize)
        self._coefficients_B = coefficients_B if coefficients_B else random() * randint(1, maxsize)
        self._data_samples_number = data_samples_number if data_samples_number else randint(data_samples_min,
                                                                                            data_samples_max)

    @property
    def data_samples_min(self):
        return self._data_samples_min

    @property
    def data_samples_max(self):
        return self._data_samples_max

    def export_to_json(self) -> Dict[str, Any]:
        ranges = {f"x{i + 1}": [self._boundaries_low[i], self._boundaries_high[i]] for i in range(self._dimensions)}
        coefficients_A = {f"x{i + 1}": self._coefficients_A[i] for i in range(self._dimensions)}
        data_samples = {"min": self._data_samples_min, "max": self._data_samples_max,
                        "number": self._data_samples_number}
        return {"ranges": ranges, "coefficients_A": coefficients_A, "coefficients_B": self._coefficients_B,
                "data_samples": data_samples}

    def generate_data_samples(self) -> np.ndarray:
        x_samples = np.random.rand(self._data_samples_number, self._dimensions)
        y_samples = np.dot(x_samples, self._coefficients_A) + self._coefficients_B
        return np.column_stack((x_samples, y_samples))

    def get_y_value(self, point: np.ndarray) -> Optional[float]:
        for i in range(self._dimensions):
            if point[i] < self._boundaries_low[i] or self._boundaries_high[i] < point[i]:
                return None
        return np.dot(point, self._coefficients_A) + self._coefficients_B

    def get_coefficients_values(self, point: np.ndarray) -> Optional[np.ndarray]:
        for i in range(self._dimensions):
            if point[i] < self._boundaries_low[i] or self._boundaries_high[i] < point[i]:
                return None
        return np.append(self._coefficients_A, self._coefficients_B)


# """
#     This class holds the information of a segment.
#     Each segment is a d- dimensional rectangle and holds a unique linear function.
#     Each the boundaries of the segments are defined by two points --
#     the lowest valued point, and the highest valued point in the rectangle.
#     ...
#
#     Attributes
#     ----------
#     d : int
#         The dimension of the space.
#
#     b_low :
#         A point in te d-dimensional space.
#         This point defines the lowest corner of the rectangle.
#
#     b_high :
#         A point in te d-dimensional space.
#         This point defines the highest corner of the rectangle.
#
#     coef_A :
#         The slope of the linear function. A d-dimensional vector.
#
#     coef_B :
#         The bias of the linear function. A d-dimensional vector.
#
#     m :
#         The number of sample points drawn within the boundaries of the segment.
#
#     Methods
#     -------
#     generate_samples()
#         This method samples a set of points from each segment and returns the points and their corresponding y-values.
#
#     get_data()
#         This method returns a dictionary with the information of the segment.
#
#     get_y(point)
#         this method returns the y-value for a queried point x.
#         If the point is outside the boundaries of the rectangle the function returns None.
# """
