import pandas as pd


class Co2Concentration:
    def __init__(self):
        self.df = pd.read_csv("data_files/co2-concentration-long-term.csv")

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
