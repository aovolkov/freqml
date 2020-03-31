import os
import pandas as pd

def load(curr1, curr2="USDT", exchange="binance", t="5m", days="1"):
    if os.path.isdir("../user_data/data/" + exchange) == False:
        os.system("cd ../user_data/data && mkdir " + exchange)
    command =   "cd ../ &&"\
              + "freqtrade download-data"\
              + " --exchange " + exchange \
              + " --pairs " + curr1 + "/" + curr2 \
              + " --datadir user_data/data/" + exchange \
              + " --days " + str(days) \
              + " -t " + t\
              + " -v --erase --dl-trades"
    os.system(command)


def load_read(curr1, curr2="USDT", exchange="binance", t="5m", days="50"):
    load(curr1, curr2="USDT", exchange="binance", t="5m", days=days)
    filename = "../user_data/data/" + exchange + "/" \
               + curr1 + "_" + curr2 + "-trades.json"
    os.system("gunzip " + filename)
    df = pd.read_json(filename)
    return df
