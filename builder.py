from generator import Generator
from ground_truth import GroundTruth
from meta_data import MetaData
from segment import Segment
from segments_generator import SegmentsGenerator
import numpy as np


class Main:
    def __init__(self, *args):
        if len(args) == 1:
            self._meta_data = self.load_from_json(args[0])
        else:
            self._meta_data = MetaData(args[0], SegmentsGenerator(args[0], args[1], args[2], args[3], args[4])
            .segments)
        self._ground_truth = GroundTruth(self._meta_data)

    @staticmethod
    def load_from_json(json) -> MetaData:
        dimensions = len(json[0][0]["coefficients"])
        segments = []
        for segment in json[0]:
            boundaries_low = [x[0] for x in segment["ranges"].values()]
            boundaries_high = [x[1] for x in segment["ranges"].values()]
            data_samples_min = segment["data_samples"]["min"]
            data_samples_max = segment["data_samples"]["max"]
            coefficients_A = [coef for coef in segment["coefficients_A"].values()]
            coefficients_B = segment["coefficients_B"]
            data_samples_number = segment["data_samples"]["number"]
            segments.append(Segment(dimensions, np.array(boundaries_low), np.array(boundaries_high), data_samples_min,
                                    data_samples_max, np.array(coefficients_A), coefficients_B, data_samples_number))
        return MetaData(dimensions, segments)

    def make_dataset_csv_file(self) -> None:
        Generator(self._meta_data).make_dataset_csv_file()

    def export_to_json(self):
        return [segment.export_to_json() for segment in self._meta_data.segments]

    def get_y_values(self, points: np.ndarray) -> np.ndarray:
        return self._ground_truth.get_y_values(points)

    def get_coefficients_values(self, points: np.ndarray) -> np.ndarray:
        return self._ground_truth.get_coefficients_values(points)
