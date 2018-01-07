#-*- coding:utf-8 –*-
from time import sleep
import os
import sys
# sys.path.append("C:\Python\scrapy\scrapy")
#import main   
import pymysql   
import os
import sys
import random
connect = pymysql.connect(
	user = "root",
	password = "512008",  
    port = 3306,
	host = "127.0.0.1",
	db = "mysql",
	charset = 'utf8mb4'
	)
con = connect.cursor()
con.execute("use librarysystem")
filename = ['yiyao.txt', 'jiankang.txt', 'jiaoyu.txt', 'jingji.txt', 'junshi.txt', 'kehuan.txt', 'meishi.txt', 'sanwen.txt', 'tonghua.txt', 'xiaoshuo.txt', 'zhengzhi.txt', 'zhexue.txt']

name = ['军事', '科幻', '美食', '散文', '童话', '政治', '哲学']
'''
for na in name:
	a = random.randint(2, 5)
	#print type(a)
	con.execute("update b set maxstore=(%d) where bk=%s"%(a, na))
	con.execute("update b set rest=(%d) where bk=%s"%(a, na))
'''
a = random.randint(2, 5)
con.execute("update b set maxstore=(%d) where bk='哲学'"%(a))
con.execute("update b set rest=(%d) where bk='哲学'"%(a))

connect.commit()
con.close()
















