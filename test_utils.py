import numpy as np

import utils as u
import matplotlib.pyplot as plt


def test_portfolio_return():
    d_weights = {'IEI': 0.1, 'VOO': 0.9}
    df_pf = u.get_portfolio_return(d_weights)
    df_pf.hist()
    plt.show()
# print(test_portfolio_return())


def test_calc_historical_vars():
    d_weights = {'IEI': 0.1, 'VOO': 0.9}
    conf_lvls= [0.99, 0.95]
    print(u.calc_historical_var(d_weights, conf_lvls))


test_calc_historical_vars()
