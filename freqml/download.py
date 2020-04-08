import os
import pandas as pd

def get_filename(curr1, curr2="USDT", exchange="binance"):
    return "../user_data/data/" + exchange + "/" \
               + curr1 + "_" + curr2 + "-trades.json"


def clear(df):
    del df['takerOrMaker']
    del df['fee']
    del df['info']
    del df['symbol']
    del df['datetime']
    del df['type']
    del df['order']
    df["id"] = df["id"] - df["id"].min()


def load(curr1, curr2="USDT", exchange="binance", t="5m", days="1"):
    if os.path.isdir("../user_data/data/" + exchange) == False:
        os.system("cd ../user_data/data && mkdir " + exchange)
    os.system("cd ../ && ./activate.sh")
    command =   "cd ../ &&"\
              + "freqtrade download-data"\
              + " --exchange " + exchange \
              + " --pairs " + curr1 + "/" + curr2 \
              + " --datadir user_data/data/" + exchange \
              + " --days " + str(days) \
              + " -t " + t\
              + " -v --erase --dl-trades"
    os.system(command)
    filename = get_filename(curr1, curr2, exchange)
    # поставить условие на удаление
    os.system("gunzip " + filename + ".gz")


def read(curr1, curr2="USDT", exchange="binance"):
    filename = get_filename(curr1, curr2, exchange)
    df = pd.read_json(filename)
    clear(df)
    return df


def load_read(curr1, curr2="USDT", exchange="binance", t="5m", days="50"):
    load(curr1, curr2, exchange, t, days)
    df = read(curr1, curr2, exchange)
    return df
