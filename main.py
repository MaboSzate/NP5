import numpy as np
import pandas as pd
import utils as u
import matplotlib.pyplot as plt

def check_etf_price():
    etf = 'VOO'
    df = u.read_etf_file(etf)
    df[['Close', 'Adj Close']].plot()
    plt.show()
# check_etf_price()


def test_return_calculation():
    u.get_etf_returns('VOO')
# test_return_calculation()


def test_plot_dividend_return():
    df = u.get_dividend_return('VOO', 'simple')
    df.plot()
    plt.show()
# test_plot_dividend_return()


def test_plot_total_return():
    df = u.get_total_return('VOO', 'log')
    df.plot()
    plt.show()


def demonstrate_historical_var(): # Value at Risk
    d_weights = {'IEI': 0.1, 'VOO': 0.9}
    df_pf = u.get_portfolio_return(d_weights)

    # sort df
    df_sorted = df_pf.sort_values(by='pf')
    df_sorted.index = [x/len(df_sorted) for x in range(1, len(df_sorted) + 1)]
    #print(df_sorted.head())
    #print(df_sorted.tail())
    print(df_sorted.quantile([0.1, 0.05, 0.025, 0.01]))  # ez is a var-t adja vissza, adott pontokra


demonstrate_historical_var()
pass