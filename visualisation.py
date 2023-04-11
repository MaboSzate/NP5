import matplotlib.pyplot as plt
import pandas as pd

import utils as u
d_weights = {'IEI': 0.6, 'VOO': 0.4}
pf_value = 100000
l_conf_levels = [0.95]
from_date = '2019-04-01'
to_date = '2020-04-01'
window_in_days = 250
df1 = u.calc_var_for_period('simple',pf_value, d_weights, l_conf_levels, from_date,to_date, window_in_days)
df1.columns=['simple']
df2 = u.calc_var_for_period('hist',pf_value, d_weights, l_conf_levels, from_date,to_date, window_in_days)
df2.columns=['hist']
df3=u.calc_var_for_period('covar',pf_value, d_weights, l_conf_levels, from_date,to_date, window_in_days)
df3.columns=['covar']
df=pd.concat([df1, df2], axis=1)
df=pd.concat([df, df3], axis=1)
df.plot()
plt.show()