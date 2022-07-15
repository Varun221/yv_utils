from tqdm.auto import tqdm
import multiprocessing as mp
import numpy as np
import pandas as pd
import os
from datetime import datetime
import pytz

import gc

""" ENV SETUP """
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

import warnings
warnings.filterwarnings('ignore')
  



""" VERIFICATION UTILS """
def run_sample_tqdm():
    for i in tqdm(range(100000)):
        pass



""" PANDAS CODE """

def _initialize_mp():
    cores = mp.cpu_count()
    print(f"Making processes faster with {cores} cores!")
    return cores


def pd_parallel_apply(Series, fun):
    cores = _initialize_mp()
    split_ser = np.array_split(Series, cores)
    with mp.Pool(cores) as p:
        app = pd.concat(p.map(fun, split_ser), axis=0)

    return app

def reduce_memory(df):
    for col in df.columns:
        col_type = df[col].dtypes
        if col_type != object:
            cmin = df[col].min()
            cmax = df[col].max()
            if str(col_type)[:3] == 'int':
                if cmin > np.iinfo(np.int8).min and cmax < np.iinfo(np.int8).max:
                    df[col] = df[col].astype(np.int8)
                elif cmin > np.iinfo(np.int16).min and cmax < np.iinfo(np.int16).max:
                    df[col] = df[col].astype(np.int16)
                elif cmin > np.iinfo(np.int32).min and cmax < np.iinfo(np.int32).max:
                    df[col] = df[col].astype(np.int32)
                elif cmin > np.iinfo(np.int64).min and cmax < np.iinfo(np.int64).max:
                    df[col] = df[col].astype(np.int64)
            else:
                if cmin > np.finfo(np.float16).min and cmax < np.finfo(np.float16).max:
                    df[col] = df[col].astype(np.float16)
                elif cmin > np.finfo(np.float32).min and cmax < np.finfo(np.float32).max:
                    df[col] = df[col].astype(np.float32)
                else:
                    df[col] = df[col].astype(np.float64)
    return df


""" SEAMLESS PYTHON EXPERIENCE """
# downloads content from drive
def download_drive(id, name):
    os.system(f"sudo wget --load-cookies /tmp/cookies.txt 'https://docs.google.com/uc?export=download&confirm=t&id={id}' -O {name} && rm -rf /tmp/cookies.txt")

def get_current_time(utc=False):
    TZ = pytz.timezone('Asia/Kolkata') if not utc else pytz.utc
    return datetime.now(TZ).strftime('%Y:%m:%d %H:%M:%S %Z %z')

# garbage collect
def gc_clear():
    gc.collect()
    for _ in range(10):
        s = gc.collect()


