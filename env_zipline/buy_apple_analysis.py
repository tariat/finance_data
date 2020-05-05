import pandas as pd

perf=pd.read_pickle('buyapple_out.pickle')

# 소수점 출력형식 조정
pd.set_option('display.float_format', '{:.2f}'.format)
perf["portfolio_value"]=perf["portfolio_value"].astype(int)
print(perf.head().T)



import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

ax1 = plt.subplot(211)

fmt = '{x:,.0f}'
tick = mtick.StrMethodFormatter(fmt)
ax1.yaxis.set_major_formatter(tick)

g=sns.lineplot(x=perf.index,y=perf["portfolio_value"], ax=ax1)

ax2 = plt.subplot(212)
sns.lineplot(x=perf.index,y=perf["AAPL"], ax=ax2)