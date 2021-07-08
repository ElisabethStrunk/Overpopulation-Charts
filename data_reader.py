import pandas as pd


class DataReader:
    def __init__(self, csv_file_path: str):
        self.df = pd.read_csv(csv_file_path)

    def full_dataframe(self) -> pd. DataFrame:
        return self.df

    def time_frame(self, start_year=None, end_year=None) -> pd.DataFrame:
        if start_year and end_year:
            return self.df[(self.df["Year"] >= start_year) & (self.df["Year"] <= end_year)]
        elif start_year and not end_year:
            return self.df[self.df["Year"] >= start_year]
        elif not start_year and end_year:
            return self.df[self.df["Year"] <= end_year]
        else:  # not start_year and not end_year
            return pd.DataFrame()


class WorldPopulation(DataReader):
    def __init__(self):
        csv_file_path = "data_files/world-population-since-10000-bce.csv"
        super().__init__(csv_file_path)
        self.df = self.df[(self.df["Entity"] == "Our World In Data") |
                          (self.df["Entity"] == "UN Medium Variant Projection (2019 revision)")]


class Co2Concentration(DataReader):
    def __init__(self):
        csv_file_path = "data_files/co2-concentration-long-term.csv"
        super().__init__(csv_file_path)


class GlobalLivingPlanetIndex(DataReader):
    def __init__(self):
        csv_file_path = "ata_files/global-living-planet-index.csv"
        super().__init__(csv_file_path)


class NaturalDisasters(DataReader):
    def __init__(self):
        csv_file_path = "data_files/number-of-natural-disaster-events.csv"
        super().__init__(csv_file_path)

    def by_disaster_type(self, disaster_type: str) -> pd.DataFrame:
        if disaster_type not in self.df["Entity"].unique():
            raise ValueError(f"No data available for disaster type {disaster_type}")
        return self.df[self.df["Entity"] == disaster_type]

    def time_frame_by_disaster_type(self, disaster_type: str, start_year=None, end_year=None) -> pd.DataFrame:
        if disaster_type not in self.df["Entity"].unique():
            raise ValueError(f"No data available for disaster type {disaster_type}")
        all_data_for_timeframe: pd.DataFrame = self.time_frame(start_year, end_year)
        return all_data_for_timeframe[all_data_for_timeframe["Entity"] == disaster_type]
