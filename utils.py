import pandas as pd
import numpy as np
import os


def read_etf_file(etf):
    filename = os.path.join('input', etf + '.csv')
    df = pd.read_csv(filename, index_col=0)
    df.index = pd.to_datetime(df.index)
    return df


def get_etf_returns(etf_name,
    return_type='log', fieldname='Adj Close'):

    df = read_etf_file(etf_name)
    df = df[[fieldname]]

    df['shifted'] = df.shift(1)
    if return_type=='log':
        df['return'] = np.log(df[fieldname]/df['shifted'])
    if return_type=='simple':
        df['return'] = df[fieldname]/df['shifted']-1
    return df[['return']]


def get_total_return(etf, return_type='log'):
    return get_etf_returns(etf, return_type, 'Adj Close')


def get_dividend_return(etf, return_type='log'):
    # 1 calc total simple return from Adj Close and Close
    df_ret_from_adj = get_etf_returns(etf, 'simple', 'Adj Close')
    df_ret_from_close = get_etf_returns(etf, 'simple', 'Close')
    # 2 simple div = ret Adj Close simple - ret Close simple
    df_div = df_ret_from_adj - df_ret_from_close
    # 3 convert to log if log
    if return_type=='log':
        df_div = np.log(df_div + 1)
    return df_div


def get_price_return(etf, return_type='log'):
    df_total = get_total_return(etf, 'simple')
    df_div = get_dividend_return(etf, 'simple')
    df_price = df_total - df_div
    if return_type == 'log':
        df_price = np.log(df_price + 1)
    return df_price



def get_portfolio_return(d_pf, return_type='log'):
    # steps
    # - join returns
    # - (drop na)
    # - (step2 multiply by weights)
    # - sum across etfs
    # - give back result
    # df_result = None
    # for etf, weight in d_pf.items():
    #     if df_result is None:
    #         df_result = weight * get_total_return(etf, 'simple')
    #     else:
    #         df_result =
    #     df_result = df_result.add(df_result, df_ret)
    # return df_result
    pass




    pass

