import pandas as pd
import numpy as np
from pandas import Series, DataFrame
import matplotlib
import matplotlib.pyplot as plt
from datetime import datetime
matplotlib.rcParams['font.family']='STSong'

df = pd.read_csv("C:\\Users\\b2utyyomi\Desktop\database\statics_kind.csv", names = ['name', 'pid', 'category'])

#读者借阅图书种类比例饼状图
category = pd.value_counts(df.category)
category_pct = category/category.sum() # 不计算也能得到饼状图
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
category_pct.plot(ax=ax, kind='pie')
ax.set_ylabel(u'')
ax.set_title(u'读者类别分布饼状图')
plt.show()
plt.savefig(u'读者类别分布饼状图.png', dpi=400)
