from meta_data import MetaData
import pandas as pd


class Generator:
    """
    This class generates a dataset given an instance of meta-data.
    ...

    Attributes
    ----------
    meta_data : MetaData
        This instance of MetaData holds the information of the segments and the corresponding linear function of each segment.

    Methods
    -------
    create_dataset()
        This function returns the samples a set of points from each segment and returns the points and their corresponding y-values.
    """

    def __init__(self, meta_data: MetaData):
        self.meta_data = meta_data

    def create_dataset(self):
        samples = [segment.generate_samples() for segment in self.meta_data.segments]
        columns = [f"x{i+1}" for i in range(self.meta_data.d)].append("y")
        df = pd.DataFrame(samples, columns=columns)
        df = df.sample(frac=1).reset_index(drop=True)
        df.to_csv("dataset.csv")
