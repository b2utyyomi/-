import scrapy
from scrapy.http import Request
import os
import sys
from time import sleep
from book.items import BookItem
import pymysql
filename = "/root/book/zhexue.txt"

class BookSpider(scrapy.Spider):
		name = 'book'
		count = 0

		start_urls = []
		def __init__(self):    
			links = open("/root/bookhref/zhexue_href.txt")  
			i = 0;
			for line in links:  
				# 一定要去掉换行符，如果有换行符则无法访问网址，真他妈坑爹  
				line=line[:-1]
				if (i>=500):
					break
				# print('-----------------------------')  
				# print('-----------------------------')  
				# print(line+'测试是否有换行符')  
				# print('-----------------------------')  
				# print('-----------------------------')  
				self.start_urls.append(line)  
				i = i+1


		'''
		def database(self,bn, au, puber, pubdate, isbn):    #调用这个自定义函数来实现对数据库的操作
			connect = pymysql.connect(
				user = "root",
				password = "512008226226",  #连接数据库，不会的可以看我之前写的连接数据库的文章
	            port = 3306,
				host = "127.0.0.1",
				db = "mysql",
				charset = "utf8"
				)
			bk = u'小说'
			bs = u'正常'
			con = connect.cursor()  #获取游标
			
			#con.execute("create database library")  #创建数据库，！！！！这一条代码仅限第一次使用，有了数据库后就不用再使用了
			con.execute("use library")   #使用数据库
			con.execute("ALTER DATABASE library CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci")
			#con.execute("drop table if exists b")  #判断是否存在这个数据库表
			
			#con.execute(create table b(isbn varchar(20) not null, bn varchar(100) not null,bk varchar(20),bs varchar(10) not null, maxstore int, rest int, author varchar(100) not null, publisher varchar(100) not null, publishdate varchar(20) not null, primary key(isbn)))  #执行sql命令  创建pages表来保存信息
			
			con.execute("ALTER TABLE b CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci")
			con.execute("ALTER TABLE b CHANGE  isbn isbn VARCHAR(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci")
			con.execute("ALTER TABLE b CHANGE bn bn VARCHAR(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci")
			con.execute("ALTER TABLE b CHANGE bk bk VARCHAR(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci")
			con.execute("ALTER TABLE b CHANGE bs bs VARCHAR(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci")
			
			con.execute("ALTER TABLE b CHANGE author author VARCHAR(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci")
			con.execute("ALTER TABLE b CHANGE publisher publisher VARCHAR(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci")
			con.execute("ALTER TABLE b CHANGE publishdate publishdate VARCHAR(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci")
						
			con.execute("insert into b(isbn,bn,bk,bs, author, publisher, publishdate) values (%s,%s, %s,%s, %s,%s, %s)",[isbn, bn, bk, bs, au, puber, pubdate])

			connect.commit()   #我们需要提交数据库，否则数据还是不能上传的
			con.close()   #关闭游标
			connect.close()  #关闭数据库
			print("OK!!!!!!!!!")
'''
		def parse(self, response):
			item = BookItem()
			#item['href'] = response.xpath('//*[@id = "content"]//h2[@class=""]//a//@href').extract()
			item['bookname']=response.xpath('//div[@id="wrapper"]//h1//span//text()').extract()
			item['author'] = response.xpath('//div[@id="info"]//a//text()').extract()
			html = response.xpath('//div[@id="info"]//text()').extract()
			bn = item['bookname']
			'''au = item['author']
			bn = bn[0]
			au = au[0]
			au = au.replace('\n', '')
			#au = au.strip()
			au = au.replace(' ', '')
			'''

			html_new = []
			f = []
			for item in html:
				item = item.replace(" ", '')
				item = item.replace('\n', '')
				item = item.replace('\xa0', '')
				if(item!=''):
					html_new.append(item)

			for i in range(len(html_new)):
				if(i<len(html_new) and html_new[i] == ':'):
					html_new[i] = ''.join(html_new[i-1])
					html_new[i-1] = ''
					html_new.remove('')
			for i in range(len(html_new)):
				if(i%2 == 1 and html_new[i-1] == '作者:'):
					f.append(html_new[i])
				if(i%2 == 1 and html_new[i-1] == '出版社:'):
					f.append(html_new[i])
				if(i%2 == 1 and html_new[i-1] == '出版年:'):
					f.append(html_new[i])
				if(i%2 == 1 and html_new[i-1] == 'ISBN:'):
					f.append(html_new[i])
			#print(f)
			au = f[0]
			puber = f[1]
			pubdate = f[2]
			isbn = f[3]
			print(bn)
			print(au)
			print(puber)
			print(pubdate)
			print(isbn)
			bk = u'哲学'
			bs = u'正常'
			f = open(filename, "a")
		
			f.write(isbn+";")
			f.write(bn[0]+";")
			f.write(bk+";")
			f.write(bs+";")
			f.write(au+";")
			f.write(puber+";")
			f.write(pubdate+"\n")
			print ("write it successfully.")
			#self.database(bn, au, puber, pubdate, isbn)
			print("Over")
			sleep(0.5)
			return item
