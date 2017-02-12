import pandas as pd
import numpy as np
import os
#from ta import ichimoku
from util import get_data, plot_data

from pandas import DataFrame, Series
from technical_analysis import ichimoku

def test_run():
    """Function called by Test Run."""
    #df = pd.read_csv("data/AAPL.csv")
    # TODO: Print last 5 rows of the data frame
    #print df.tail()
    # slice adjust price
    
    start_date = '2007-12-31'
    end_date = '2009-12-31'
    df = get_data(['AAPL'], pd.date_range(start_date, end_date), addSPY=False)
    #print df.tail()
    df = df['AAPL'].dropna()
    #print ichimoku(df['AAPL'].dropna())
    plot_data(ichimoku(df))
    
    

if __name__ == "__main__":
    test_run()