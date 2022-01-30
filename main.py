from meta_data import MetaData
from type import Type
from segment import Segment
from generator import Generator
from typing import List
from ground_truth import GroundTruth

class Main:
    def __init__(self, d: int, data_type: Type, noise: int):
        self.meta_data = MetaData(d, self.create_segments(), data_type, noise)

    @staticmethod
    def create_segments():
        return [Segment] # get segments

    def create_dataset(self):
        Generator(self.meta_data).create_dataset()

    def get_data(self):
        return [segment.get_data() for segment in self.meta_data.segments]

    def get_y(self, point: List):
        return GroundTruth(self.meta_data).get_y(point)







