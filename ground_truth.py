from meta_data import MetaData
import numpy as np

"""
    This class is used for returning  the y-value for a queried x.
    ...
    
    Attributes
    ----------
    meta_data : MetaData
        This instance of MetaData holds the information of the segments and the corresponding linear function of each 
        segment.
    
    Methods
    -------
    get_y(point: List)
        This function returns the y-value for a queried x.
"""


class GroundTruth:
    def __init__(self, meta_data: MetaData):
        self._meta_data = meta_data

    def get_y_values(self, points: np.ndarray) -> np.ndarray:
        return self._meta_data.get_y_values(points)

    def get_coefficients_values(self, points: np.ndarray) -> np.ndarray:
        return self._meta_data.get_coefficients_values(points)
