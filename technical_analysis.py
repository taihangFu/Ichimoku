import numpy as np
from pandas import DataFrame, Series


def hhv(s, n):
    return Series.rolling(s, n).max()

def llv(s, n):
    return Series.rolling(s, n).min()

    
#ichimoku
def ichimoku(s, n1=9, n2=26, n3=52):

    conv = (hhv(s, n1) + llv(s, n1)) / 2
    base = (hhv(s, n2) + llv(s, n2)) / 2

    spana = (conv + base) / 2
    spanb = (hhv(s, n3) + llv(s, n3)) / 2
    k = s
    return DataFrame(dict(k=k,conv=conv, base=base, spana=spana.shift(n2),
                          spanb=spanb.shift(n2), lspan=s.shift(-n2)))
