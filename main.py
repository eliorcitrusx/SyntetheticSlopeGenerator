from json import load
from typing import List, Dict
import numpy as np
from meta_data import MetaData
from data_type import DataType
from segment import Segment
from generator import Generator


def create_meta_data(dimensions: int, data_type: DataType, noise_level: float, boundaries_low: List,
                     boundaries_high: List, data_samples_min: int, data_samples_max: int) -> None:
    MetaData(dimensions, data_type, noise_level, boundaries_low, boundaries_high, data_samples_min,
             data_samples_max).export_to_json()


def generate_train_dataset(json_file_name: str):
    with open(json_file_name, 'r') as file:
        json = load(file)
    meta_data = _generate_meta_data_from_json(json, True)
    train_file_name = ""  # add file name
    Generator.make_dataset_csv_file(meta_data, train_file_name)


def generate_test_dataset(json_file_name: str, data_samples_number: int):
    with open(json_file_name, 'r') as file:
        json = load(file)
    meta_data = _generate_meta_data_from_json(json, False, data_samples_number)
    test_file_name = ""  # add file name
    Generator.make_dataset_csv_file(meta_data, test_file_name)


def _generate_meta_data_from_json(json: Dict, is_train: bool, test_data_samples_number: int = None) -> MetaData:
    dimensions = json["dimensions"]
    data_type = json["data_type"]
    noise_level = json["noise_level"]
    segments = []
    for segment in json["segments"]:
        boundaries_low = [x[0] for x in segment["ranges"].values()]
        boundaries_high = [x[1] for x in segment["ranges"].values()]
        data_samples_min = segment["data_samples"]["min"] if is_train else test_data_samples_number
        data_samples_max = segment["data_samples"]["max"] if is_train else test_data_samples_number
        coefficients_A = [coef for coef in segment["coefficients_A"].values()]
        coefficients_B = segment["coefficients_B"]
        data_samples_number = segment["data_samples"]["number"] if is_train else test_data_samples_number
        segments.append(Segment(dimensions, np.array(boundaries_low), np.array(boundaries_high), data_samples_min,
                                data_samples_max, np.array(coefficients_A), coefficients_B, data_samples_number))
    return MetaData(dimensions, data_type, noise_level, segments)
