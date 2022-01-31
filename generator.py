import pandas as pd
from meta_data import MetaData


class Generator:
    def __init__(self, ):
        pass

    @staticmethod
    def make_dataset_csv_file(meta_data: MetaData, file_name: str) -> None:
        data_samples = [segment.generate_data_samples() for segment in meta_data.segments]
        columns = [f"x{i+1}" for i in range(meta_data.dimensions)].append("y")
        df = pd.DataFrame(data_samples, columns=columns)
        df = df.sample(frac=1).reset_index(drop=True)
        df.to_csv(file_name)

    # """
    # This class generates a dataset given an instance of meta-data.
    # ...
    #
    # Attributes
    # ----------
    # meta_data : MetaData
    #     This instance of MetaData holds the information of the segments and the corresponding linear function of each
    #     segment.
    #
    # Methods
    # -------
    # create_dataset()
    #     This function returns the samples a set of points from each segment and returns the points and their
    #     corresponding y-values.
    # """
