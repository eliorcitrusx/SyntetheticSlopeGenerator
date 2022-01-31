from json import dump
from typing import List
import numpy as np
from itertools import product
from segment import Segment


class MetaData:
    def __init__(self, *args):
        self._dimensions = args[0]
        self._data_type = args[1]
        self._noise_level = args[2]
        if len(args) != 4:
            self._segments = self._generate_segments(args[3], args[4], args[5], args[6])
        else:
            self._segments = args[3]

    @property
    def dimensions(self):
        return self._dimensions

    @property
    def segments(self):
        return self._segments

    def _generate_segments(self,
                           boundaries_low: List,
                           boundaries_high: List,
                           data_samples_min: int,
                           data_samples_max: int) -> List[Segment]:
        x_boundaries_low = [np.arange(boundaries_low[i], boundaries_high[i] - 1, 1) for i in range(self._dimensions)]
        x_boundaries_high = [np.arange(boundaries_low[i] + 1, boundaries_high[i], 1) for i in range(self._dimensions)]
        low_edges = [low_edge for low_edge in product(*x_boundaries_low)]
        high_edges = [high_edge for high_edge in product(*x_boundaries_high)]
        return [Segment(self._dimensions, low_edges[i], high_edges[i], data_samples_min, data_samples_max)
                for i in range(len(low_edges))]

    def export_to_json(self):
        dictionary = {"dimensions": self._dimensions, "data_type": self._data_type, "noise_level": self._noise_level,
                      "segments": [segment.export_to_json() for segment in self._segments]}
        with open("file_name.json", "w") as file:  # create proper file name
            dump(dictionary, file)

    def get_y_values(self, points: np.ndarray) -> np.ndarray:
        y_values = np.zeros(shape=(points.shape[0], 1), dtype=float)
        for i, point in enumerate(points):
            if len(point) != self._dimensions:
                raise ValueError("A point must have the same dimensions as its dimensions")
            for segment in self._segments:
                y = segment.get_y_value(point)
                if y:
                    y_values[i] = y
                    break
        return y_values

    def get_coefficients_values(self, points: np.ndarray) -> np.ndarray:
        coefficients_values = np.zeros(shape=(points.shape[0], self._dimensions), dtype=float)
        for i, point in enumerate(points):
            if len(point) != self._dimensions:
                raise ValueError("A point must have the same dimensions as its dimensions")
            for segment in self._segments:
                coefficients = segment.get_coefficients_values(point)
                if coefficients:
                    for j, value in enumerate(coefficients):
                        coefficients_values[i][j] = value
                    break
        return coefficients_values

# """
#     This class holds the information about the space and its partition to segments.
#     ...
#
#     Attributes
#     ----------
#     d : int
#         The dimension of the space.
#
#     segments : List[Segment]
#         A list of non-overlapping segments. Each segment is defined by its boundaries and holds a linear function.
#
#     type : Type(ENUM)
#         The type of labels needs to be recognized by the Citron tree.
#         The type is either categorical, continuous, or binary.
#
#     Methods :
#     -------
#     d()
#         Returns the dimension of the space.
#
#     segments()
#         Returns a list of the segments defined by the partition. Each segments holds its boundaries and a linear
#         function.
#
#     get_y(point: List)
#         given a query point, finds the corresponding segment and returns the label obtained for the query point
#         by the linear function defined  in the segment.
#         If the query point is not part of the space, the function returns None.
# """
