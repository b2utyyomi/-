#-*- coding:utf-8 –*-
import csv
import os
import sys
import pymysql
# 将数据库中的必要信息写进csv

#其实这里是有一个问题的，我的设计是还一本书，借书记录就要去掉这本书的信息，
#但是对于统计来讲，这样哪里能行，读者几个月前的借书记录是会被删掉的，所以有必要做一个阅读记录表
#再说吧，看我心情。


#统计某一时间段(2017年下半年)最受欢迎的图书类型。
#

dirname = "C:\\Users\\b2utyyomi\Desktop\database\\"
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
con.execute("select bk, b_date from b_r, b where b_r.isbn=b.isbn and b_date like '2017%'")
ans = con.fetchall()
lst = []
with open(dirname+'book_statics.csv', 'w+', encoding="utf-8") as csvfile:
	writer = csv.writer(csvfile)
	for i in ans:
		writer.writerow(i)
		#print (i)
	

connect.commit()   
con.close()  
connect.close()  
print("OK!!!!!!!!!")















