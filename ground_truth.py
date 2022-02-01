from meta_data import MetaData
import numpy as np


class GroundTruth:
    def __init__(self, meta_data: MetaData):
        self._meta_data = meta_data

    def predict(self, points: np.ndarray) -> np.ndarray:
        return self._meta_data.predict(points)

    def get_coefficients_values(self, points: np.ndarray) -> np.ndarray:
        return self._meta_data.coefficients(points)

# """
#     This class is used for returning  the y-value for a queried x.
#     ...
#
#     Attributes
#     ----------
#     meta_data : MetaData
#         This instance of MetaData holds the information of the segments and the corresponding linear function of each
#         segment.
#
#     Methods
#     -------
#     get_y(point: List)
#         This function returns the y-value for a queried x.
# """
