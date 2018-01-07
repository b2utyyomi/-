import pandas as pd
import numpy as np
from pandas import Series, DataFrame
import matplotlib
import matplotlib.pyplot as plt
from datetime import datetime
matplotlib.rcParams['font.family']='STSong'

df = pd.read_csv('C:\\Users\\b2utyyomi\Desktop\database\statics_r.csv', names = ['rn', 'bk'])

# 2017年11-12月活跃读者前十名
reader = pd.value_counts(df.rn)[:10]
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
reader.plot(ax=ax, kind='bar', color='cornflowerblue', rot = 0)
ax.set_xlabel(u'读者姓名')
ax.set_ylabel(u'借阅数量')
ax.set_title(u'2017年11-12月活跃读者前十名柱状图')
plt.savefig(u'2017年11-12月活跃读者前十名柱状图.png', dpi=400)
plt.show()
