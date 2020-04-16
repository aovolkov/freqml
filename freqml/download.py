import os
import pandas as pd
from freqml.json2csv import json2csv

abs_path = os.path.abspath(__file__)
freqml_path = "/".join(abs_path.split("/")[:-2])
freqtr_user_path = freqml_path + "/freqtrade/user_data/data/"


def get_filepath(curr1, curr2="USDT", days="1", exchange="binance"):
    path = freqtr_user_path + exchange + "/"
    file = curr1 + "_" + curr2 + "-trades--" + days + "d" + ".csv"
    return path + file


def clear(df):
    del df['takerOrMaker']
    del df['fee']
    del df['info']
    del df['symbol']
    del df['datetime']
    del df['type']
    del df['order']
    df["id"] = df["id"] - df["id"].min()


def load(curr1, curr2="USDT", exchange="binance", days="1"):
    filepath = get_filepath(curr1, curr2, days, exchange)
    if os.path.isfile(filepath) == True:
        os.remove(filepath)
    command =   "cd " + freqml_path + "/freqtrade &&"\
              + "freqtrade download-data"\
              + " --exchange " + exchange \
              + " --pairs " + curr1 + "/" + curr2 \
              + " --datadir user_data/data/" + exchange \
              + " --days " + str(days) \
              + " -v --erase --dl-trades"
    os.system(command)
    os.system("gunzip " + filepath.split("--")[0] + ".json.gz")
    json2csv(filepath.split("--")[0] + ".json",
             filepath)
    os.system("cd " + freqtr_user_path + exchange + "/ &&" \
              + "rm " + "*.json")


def read(curr1, curr2="USDT", exchange="binance", days="1", override=False):
    filepath = get_filepath(curr1=curr1, curr2=curr2, days=days, exchange=exchange)
    if os.path.isfile(filepath) == False or override == True:
        load(curr1, curr2, exchange, days)
    df = pd.read_csv(filepath)
    clear(df)
    return df


def big_read(curr1, curr2="USDT", exchange="binance", days="1", override=False):
    filepath = get_filepath(curr1=curr1, curr2=curr2, days=days, exchange=exchange)
    if os.path.isfile(filepath) == False or override == True:
        load(curr1, curr2, exchange, days)
    df_parted = pd.read_csv(filepath, chunksize=1000000)
    return df_parted