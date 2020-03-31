import pandas as pd
import numpy as np
@pd.api.extensions.register_dataframe_accessor("bars")
class bars:
    def __init__(self, df):
        self._validate(df)
        self._df = df
        self._shape = df.shape

    @staticmethod
    def _validate(obj):
        # verify there is a column latitude and a column longitude
        if 'latitude' not in obj.columns or 'longitude' not in obj.columns:
            raise AttributeError("Must have 'latitude' and 'longitude'.")

    @property
    def TB(self, m):
        self._df = self._df[:-self._shape[0] % m]
        df_TB = self._df.groupby(np.floor(self._df["id"]/m)).mean()

        return df_TB

    def VB(self):
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