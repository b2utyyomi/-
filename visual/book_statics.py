import pandas as pd
import numpy as np
from pandas import Series, DataFrame
import matplotlib
import matplotlib.pyplot as plt
from datetime import datetime
matplotlib.rcParams['font.family']='STSong'

df = pd.read_csv("C:\\Users\\b2utyyomi\Desktop\database\\book_statics.csv", names=['kind', 'b_date'])

# 2017年下半年最受读者欢迎的前五类图书
category = pd.value_counts(df.kind)[:5]
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
category.plot(ax=ax, kind='bar', color='cornflowerblue', rot = 0)
ax.set_xlabel(u'图书类别')
ax.set_ylabel(u'借阅数量')
ax.set_title(u'2017年下半年最受读者欢迎的前五类图书柱状图')
plt.savefig(u'2017年下半年最受读者欢迎的前五类图书柱状图1.png', dpi=400)
plt.show()

#读者借阅图书种类比例饼状图
category = pd.value_counts(df.kind)
category_pct = category/category.sum() # 不计算也能得到饼状图
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
category_pct.plot(ax=ax, kind='pie')
ax.set_ylabel(u'')
ax.set_title(u'读者借阅图书种类比例饼状图')
plt.savefig(u'读者借阅图书种类比例饼状图.png', dpi=400)

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

reader_bk = pd.crosstab(df.rn, df.bk)
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
reader_bk[:10].plot(ax=ax, kind='barh', rot=0, stacked = True)
ax.set_ylabel(u'读者姓名')
ax.set_xlabel(u'借阅数量')
ax.set_title(u'活跃读者读书偏好堆积柱状图')
ax.legend(loc='best', title=u'图书类别')
plt.savefig(u'活跃读者读书偏好堆积柱状图.png', dpi=400)











