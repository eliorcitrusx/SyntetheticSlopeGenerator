from meta_data import MetaData
from segment import Segment
from generator import Generator
from typing import List
from ground_truth import GroundTruth
from segments_generator import SegmentsGenerator
import numpy as np


class Main:
    def __init__(self, *args):
        if len(args) == 1:
            d = len(args[0]["coefficients"])
            segments = []
            for segment in args[0]:
                b_low = [x[0] for x in segment["ranges"].values()]
                b_high = [x[1] for x in segment["ranges"].values()]
                coef_A = [coef[0] for coef in segment["coefficients"].values()]
                coef_B = list(segment["coefficients"].values())[0][1]
                m = segment["m"]
                segments.append(Segment(d, np.array(b_low), np.array(b_high), np.array(coef_A), coef_B, m))
            self.meta_data = MetaData(d, segments)
        else:
            self.meta_data = MetaData(args[0], SegmentsGenerator(args[1], args[2], args[3]).segments,
                                      args[4])

    def create_dataset(self):
        Generator(self.meta_data).create_dataset()

    def get_data(self):
        return [segment.get_data() for segment in self.meta_data.segments]

    def get_y(self, point: List):
        return GroundTruth(self.meta_data).get_y(point)
