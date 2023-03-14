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
# test_plot_total_return()


def test_portfolio_return():
    d_pf = {'VOO': 0.6, 'IEI': 0.4}
    u.get_portfolio_return(d_pf, 'simple')
test_portfolio_return()