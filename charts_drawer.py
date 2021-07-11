import matplotlib.pyplot as plt
import pandas as pd


class ChartDrawer:
    @staticmethod
    def line_chart(data_frame: pd.DataFrame):
        data_frame.plot(x="Year")
        plt.show()


if __name__ == "__main__":
    from data_reader import WorldPopulation

    df = WorldPopulation().full_dataframe()
    ChartDrawer.line_chart(df)
