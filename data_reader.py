import pandas as pd


class DataReader:
    def __init__(self, csv_file_path: str):
        self.df = pd.read_csv(csv_file_path)

    def full_dataframe(self) -> pd. DataFrame:
        return self.df

    def time_frame(self, start_year=None, end_year=None) -> pd.DataFrame:
        if start_year and end_year:
            return self.df.loc[self.df["Year"] >= start_year & self.df["Year"] <= end_year]
        elif start_year and not end_year:
            return self.df.loc[self.df["Year"] >= start_year]
        elif not start_year and end_year:
            return self.df.loc[self.df["Year"] <= end_year]
        else:  # not start_year and not end_year
            return pd.DataFrame()


class Co2Concentration(DataReader):
    def __init__(self):
        csv_file_path = "data_files/co2-concentration-long-term.csv"
        super().__init__(csv_file_path)
