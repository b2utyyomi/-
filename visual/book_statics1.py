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











