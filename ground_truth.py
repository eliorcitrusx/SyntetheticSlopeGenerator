from meta_data import MetaData
import numpy as np


class GroundTruth:
    def __init__(self):
        pass

    @staticmethod
    def get_y_values(meta_data: MetaData, points: np.ndarray) -> np.ndarray:
        return meta_data.get_y_values(points)

    @staticmethod
    def get_coefficients_values(meta_data: MetaData, points: np.ndarray) -> np.ndarray:
        return meta_data.get_coefficients_values(points)

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
