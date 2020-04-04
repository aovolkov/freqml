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

    @property
    def dvolume(self):
        return self._df["cost"].sum()

    #@staticmethod
    def make_bars(grouped):
        df = grouped["price"].ohlc()
        df["amount"] = grouped["amount"].sum()
        df["VWAP"] = grouped["cost"].sum() / df["amount"]
        df = df.set_index(grouped["timestamp"].nth(-1))
        return df

    def TB(self, m=100):
        if self._shape[0] % m != 0:
            self._df = self._df[:-(self._shape[0] % m)]
        grouped = self._df.groupby(np.floor(self._df["id"] / m))
        df_TB = bars.make_bars(grouped)
        return df_TB

    def VB(self, v=5000):
        self._df["amount_cumsum"] = self._df["amount"].cumsum()
        df_VB = self._df[self._df["amount_cumsum"] <= np.floor(self.volume - (self.volume % v))]
        grouped = df_VB.groupby(np.floor(df_VB["amount_cumsum"] / v))
        del self._df["amount_cumsum"]
        df_VB = bars.make_bars(grouped)
        return df_VB

    def DB(self, d=10000):
        self._df["cost_cumsum"] = self._df["cost"].cumsum()
        df_DB = self._df[self._df["cost_cumsum"] <= np.floor(self.dvolume - (self.dvolume % d))]
        grouped = df_DB.groupby(np.floor(df_DB["cost_cumsum"] / d))
        del self._df["cost_cumsum"]
        df_DB = bars.make_bars(grouped)
        return df_DB

    def TIB(self):
        pass
        # return bars.TB(T)

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