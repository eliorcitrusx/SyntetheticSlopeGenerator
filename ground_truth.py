from typing import List, Optional
from meta_data import MetaData


class GroundTruth:
    def __init__(self, meta_data: MetaData):
        self._meta_data = meta_data

    def get_y_value(self, point: List) -> Optional[float]:
        return self._meta_data.get_y_value(point)
