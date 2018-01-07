import pandas as pd
import numpy as np
from pandas import Series, DataFrame
import matplotlib
import matplotlib.pyplot as plt
from datetime import datetime
matplotlib.rcParams['font.family']='STSong'

df = pd.read_csv('C:\\Users\\b2utyyomi\Desktop\database\statics_r.csv', names = ['rn', 'bk'])

reader_bk = pd.crosstab(df.rn, df.bk)
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
reader_bk[:10].plot(ax=ax, kind='barh', rot=0, stacked = True)
ax.set_ylabel(u'读者姓名')
ax.set_xlabel(u'借阅数量')
ax.set_title(u'活跃读者读书偏好堆积柱状图')
ax.legend(loc='best', title=u'图书类别')
plt.savefig(u'活跃读者读书偏好堆积柱状图.png', dpi=400)
plt.show()