#-*- coding:utf-8 –*-
from time import sleep
import os
import sys
# sys.path.append("C:\Python\scrapy\scrapy")
#import main   
import pymysql   
import os
import sys



dirname = "C:\Users\\b2utyyomi\Desktop\database\\book_1\\book\\"
filename = ['yiyao.txt', 'jiankang.txt', 'jiaoyu.txt', 'jingji.txt', 'junshi.txt', 'kehuan.txt', 'meishi.txt', 'sanwen.txt', 'tonghua.txt', 'xiaoshuo.txt', 'zhengzhi.txt', 'zhexue.txt']
connect = pymysql.connect(
	user = "root",
	password = "512008",  
    port = 3306,
	host = "127.0.0.1",
	db = "mysql",
	charset = 'utf8mb4'
	)
con = connect.cursor()  

#con.execute("create database qcwy_tag")  
con.execute("use librarysystem")   
con.execute("ALTER DATABASE librarysystem CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci")
con.execute("ALTER TABLE b CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci")
con.execute("ALTER TABLE b CHANGE isbn isbn VARCHAR(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci")
con.execute("ALTER TABLE b CHANGE bn bn VARCHAR(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci")
con.execute("ALTER TABLE b CHANGE bk bk VARCHAR(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci")
con.execute("ALTER TABLE b CHANGE bs bs VARCHAR(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci")
con.execute("ALTER TABLE b CHANGE author author VARCHAR(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci")
con.execute("ALTER TABLE b CHANGE publisher publisher VARCHAR(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci")
con.execute("ALTER TABLE b CHANGE publishdate publishdate VARCHAR(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci")
for file in filename:
	with open(dirname+file,"r") as f:  
		while True:
			info = f.readline()   
			if info:
				info = info.strip() 
				info = info.split(";")  
				isbn = info[0]
				bn = info[1]
				bk = info[2]
				bs = info[3]
				author = info[4]
				publisher = info[5]
				publishdate = info[6]
				#如果记录中有这条数据那么就不插要怎么控制？
				ans = con.execute("select * from b where isbn=(%s)",isbn)
				if (ans):
					continue
				con.execute("insert into b(isbn, bn, bk, bs, author, publisher, publishdate) values (%s,%s,%s,%s, %s, %s, %s)",([isbn, bn, bk, bs, author, publisher, publishdate]))
				
			else:
				break
connect.commit()   
con.close()  
connect.close()  
print("OK!!!!!!!!!")















