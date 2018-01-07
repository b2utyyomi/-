#-*- coding:utf-8 –*-
from time import sleep
import os
import sys
import pymysql   
import random

# 做很多借书记录
connect = pymysql.connect(
	user = "root",
	password = "512008",  
    port = 3306,
	host = "127.0.0.1",
	db = "mysql",
	charset = 'utf8mb4'
	)

con = connect.cursor()  

isbn= 9787502581091
bk = u'医学'
b_count = 1
con.execute("use librarysystem")   

#day = ['2017-11-03', '2017-11-05', '2017-11-10', '2017-11-15', '2017-11-16', '2017-11-28', '2017-12-03',
#'2017-12-15', '2017-12-22', '2017-12-31']
day = ['2017-01-01', '2017-01-02']
for d1 in day:
	for i in range(50):
		b = random.randint(0, 2256);
		r = random.randint(15, 22);
		con.execute("select * from b")
		book = con.fetchall()
		con.execute("select * from reader")
		reader = con.fetchall()
		print(r)
		category = reader[r][3]
		con.execute("select * from kind where kno = '"+ category+"'")
		kind = con.fetchall()
		max_b = kind[0][3]
		print(reader[r])
		print(max_b)
		con.execute("select count(pid) from b_r where pid = '"+ reader[r][1]+ "'")
		pid_count = con.fetchall()
		max_count = pid_count[0][0]
		if(book[b][5] == 0 or max_count == max_b):
			continue
		#con.execute("insert into b_r(pid, isbn, b_date, b_count) values (%s,%s,%s,%d)",([reader[r][1], book[b][0], d1, b_count]))
		con.execute("insert into b_r(pid, isbn, b_date, b_count) values ('"+reader[r][1]+"','"+book[b][0]+"','"+d1+"',"+"%d)"%(b_count))
		con.execute("update b set rest = rest-1 where isbn = '"+book[b][0]+"'")

			
connect.commit()   
con.close()  
connect.close()  
print("OK!!!!!!!!!")















