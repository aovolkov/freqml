import pandas as pd
import numpy as np
@pd.api.extensions.register_dataframe_accessor("bars")
class bars:
    def __init__(self, df):
       self._df = df

    @property
    def _shape(self):
        return self._df.shape

    @property
    def volume(self):
        return self._df["amount"].sum()

    def TB(self, m=100):
        if self._shape[0] % m != 0:
            self._df = self._df[:-(self._shape[0] % m)]
        grouped = self._df.groupby(np.floor(self._df["id"] / 100))
        df_TB = grouped["price"].ohlc()
        df_TB["amount"] = grouped["amount"].sum()
        df_TB["VWAP"] = grouped["cost"].sum() / df_TB["amount"]
        df_TB = df_TB.set_index(grouped["timestamp"].nth(0))
        return df_TB

    def VB(self, v=10000):
        # if int(self.volume) % int(v) != 0:
        #     self._df = self._df[:-(self.volume % v)]
        # grouped = self._df.groupby(np.floor(self._df["id"] / 100))
        # df_TB = grouped["price"].ohlc()
        # df_TB["amount"] = grouped["amount"].sum()
        # df_TB["VWAP"] = grouped["cost"].sum() / df_TB["amount"]
        # df_TB = df_TB.set_index(grouped["timestamp"].nth(0))
        # return df_TB
        pass

    def DB(self):
        pass

    def TIB(self):
        pass

    def VIB(self):
        pass

    def DIB(self):
        pass

    def TRB(self):
        pass

    def VRB(self):
        pass

    def DRB(self):
        pass