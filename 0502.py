import numpy as np
import matplotlib.pyplot as plt


def calc_cov(corr, sigma1, sigma2):
    var1 = sigma1**2
    var2 = sigma2**2
    cov12 = corr*sigma1*sigma2
    cov = np.matrix([[var1, cov12], [cov12, var2]])
    return cov


def calc_returns(mu, cov):
    folytonos = np.random.multivariate_normal(mu, cov, n)
    effektiv = np.exp(folytonos)-1
    return effektiv


def calc_pf_returns(returns, weights):
    return np.dot(returns, weights)


cov = calc_cov(0.1, 0.2, 0.05)
mu = [0.05, 0.02]
n = 1000
price = [100, 200]
w = np.array([0.4, 0.6])
returns = calc_returns(mu, cov)
print(returns.mean(axis=0), returns.std(axis=0))
# plt.scatter(returns[:, 0], returns[:, 1])
# plt.show()
pf_returns = calc_pf_returns(returns, w)
pass





