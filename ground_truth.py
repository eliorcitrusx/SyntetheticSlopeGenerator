from meta_data import MetaData
from typing import List


class GroundTruth:
    def __init__(self, meta_data: MetaData):
        self._meta_data = meta_data

    def get_y(self, point: List):
        return self._meta_data.get_y(point)
