import yv_utils.main as yv
import pandas as pd
import numpy as np

def fun(x):
    return x+1


if __name__ == '__main__':
    g = yv.downLoad_glove()
    print(g['help'].shape)