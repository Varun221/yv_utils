from tqdm.auto import tqdm
import multiprocessing as mp
import numpy as np
import pandas as pd
import os
from datetime import datetime
import pytz
  



""" VERIFICATION UTILS """
def run_sample_tqdm():
    for i in tqdm(range(100000)):
        pass



""" FASTER CODE """

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


""" SEAMLESS PYTHON EXPERIENCE """
# downloads content from drive
def download_drive(id, name):
    os.system(f"sudo wget --load-cookies /tmp/cookies.txt 'https://docs.google.com/uc?export=download&confirm=t&id={id}' -O {name} && rm -rf /tmp/cookies.txt")

def get_current_time(utc=False):
    TZ = pytz.timezone('Asia/Kolkata') if not utc else pytz.utc
    return datetime.now(TZ).strftime('%Y:%m:%d %H:%M:%S %Z %z')