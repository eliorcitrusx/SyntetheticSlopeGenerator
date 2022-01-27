from meta_data import MetaData
import pandas as pd


class Generator:
    def __int__(self, meta_data: MetaData):
        self.create_dataset(meta_data)

    @staticmethod
    def create_dataset(meta_data: MetaData):
        samples = [segment.generate_samples() for segment in meta_data.segments]
        columns = [f"x{i+1}" for i in range(meta_data.d)].append("y")
        df = pd.DataFrame(samples, columns=columns)
        df = df.sample(frac=1).reset_index(drop=True)
        df.to_csv("dataset.csv")

