import numpy as np

import utils as u
import matplotlib.pyplot as plt
import seaborn as sns


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
# test_plot_total_return()


def test_portfolio_return():
d_pf = {'VOO': 0.6, 'IEI': 0.4}
u.get_portfolio_return(d_pf)
# test_portfolio_return()


def demonstrate_list_comprehension():
xs = [1, 2, 5]
# using normal for
result1 = []
for x in xs:
result1.append(x*2)
print(result1)
# using list comprehension
result2 = [x * 2 for x in xs]
print(result2)
# demonstrate_list_comprehension()


def demonstrate_historical_var():
d_weights = {'IEI': 0.1, 'VOO': 0.9}
df_pf = u.get_portfolio_return(d_weights)
# calculate percentile by using calculated index
df_sorted = df_pf.sort_values(by='pf')
df_sorted.index = [x/len(df_sorted) for x in range(1, len(df_sorted)+1)]
print(df_sorted.head(20))
# calculate var by using quantile
print(df_pf.quantile([0.1, 0.05, 0.025, 0.01]))


demonstrate_historical_var()