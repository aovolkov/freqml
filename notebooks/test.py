from freqml import *
import pandas as pd
import numpy as np

df = download.load_read("ETH")
ds = pd.DataFrame({'longitude': np.linspace(0, 10),
                   'latitude': np.linspace(0, 20)})
f = ds.bars.center
j = ds.bars.plot()