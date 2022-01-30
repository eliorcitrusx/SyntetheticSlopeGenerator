from typing import List, Optional
from generator import Generator
from ground_truth import GroundTruth
from meta_data import MetaData
from segment import Segment
from segments_generator import SegmentsGenerator
import numpy as np


class Main:

    """A bird with a flight speed exceeding that of an unladen swallow.

    Attributes:
        flight_speed     The maximum speed that such a bird can attain.
        nesting_grounds  The locale where these birds congregate to reproduce.
    """
    def __init__(self, *args):
        if len(args) == 1:
            self._meta_data = self.load_from_json(args[0])
        else:
            self._meta_data = MetaData(args[0], SegmentsGenerator(args[0], args[1], args[2]).segments)

    @staticmethod
    def load_from_json(json) -> MetaData:
        dimensions = len(json[0][0]["coefficients"])
        segments = []
        for segment in json[0]:
            boundaries_low = [x[0] for x in segment["ranges"].values()]
            boundaries_high = [x[1] for x in segment["ranges"].values()]
            coefficients_A = [coef for coef in segment["coefficients_A"].values()]
            coefficients_B = segment["coefficients_B"]
            data_samples_number = segment["data_samples_number"]
            segments.append(Segment(dimensions, np.array(boundaries_low), np.array(boundaries_high),
                                    np.array(coefficients_A), coefficients_B, data_samples_number))
        return MetaData(dimensions, segments)

    def make_dataset_csv_file(self) -> None:
        Generator(self._meta_data).make_dataset_csv_file()

    def export_to_json(self):
        return [segment.export_to_json() for segment in self._meta_data.segments]

    def get_y_value(self, point: List) -> Optional[float]:
        return GroundTruth(self._meta_data).get_y_value(point)
