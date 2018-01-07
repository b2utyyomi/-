#-*- coding:utf-8 –*-
import os
import sys
import pandas as pd
import numpy as np
dirname="C:\\Users\\b2utyyomi\Desktop\database\\book_1\\book\\"
filename = ['yiyao.txt', 'jiankang.txt', 'jiaoyu.txt', 'jingji.txt', 'junshi.txt', 'kehuan.txt', 'meishi.txt', 'sanwen.txt', 'tonghua.txt', 'xiaoshuo.txt', 'zhengzhi.txt', 'zhexue.txt']

for file in filename:
	dir_ = dirname + file;
	txt = np.loadtxt(dir_, 'rb')
	txtDF = pd.DataFrame(txt)	
	txtDF.to_scv('book.csv', index=False)
