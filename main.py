from meta_data import MetaData
from type import Type
from segment import Segment
from generator import Generator
from typing import List
from ground_truth import GroundTruth
from segments_generator import SegmentsGenerator

class Main:
    def __init__(self, *args):
        if len(args) == 1:
            self.meta_data = 0  # get segments from json
        else:
            self.meta_data = MetaData(args[0], SegmentsGenerator(args[1], args[2], args[3]), args[4]) # get segments

    @staticmethod
    def create_segments():
        return [Segment] # get segments

    def create_dataset(self):
        Generator(self.meta_data).create_dataset()

    def get_data(self):
        return [segment.get_data() for segment in self.meta_data.segments]

    def get_y(self, point: List):
        return GroundTruth(self.meta_data).get_y(point)







