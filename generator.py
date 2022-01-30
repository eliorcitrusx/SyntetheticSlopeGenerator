import pandas as pd
from meta_data import MetaData


class Generator:
    def __init__(self, meta_data: MetaData):
        self._meta_data = meta_data

    def make_dataset_csv_file(self) -> None:
        data_samples = [segment.generate_data_samples() for segment in self._meta_data.segments]
        columns = [f"x{i+1}" for i in range(self._meta_data.dimensions)].append("y")
        df = pd.DataFrame(data_samples, columns=columns)
        df = df.sample(frac=1).reset_index(drop=True)
        df.to_csv("dataset.csv")
