# _*_ coding:utf-8 _*_
from time import sleep
import os
import sys
import csv
dirname = "C:\\Users\\b2utyyomi\Desktop\database\\book_1\\book\\"
filename = ['yiyao.txt', 'jiankang.txt', 'jiaoyu.txt', 'jingji.txt', 'junshi.txt', 'kehuan.txt', 'meishi.txt', 'sanwen.txt', 'tonghua.txt', 'xiaoshuo.txt', 'zhengzhi.txt', 'zhexue.txt']
i = 0
j = 0;
with open('book.csv', 'w+') as csvfile:
	writer = csv.writer(csvfile)
	for file in filename:
		dir = dirname + file

		with open(dir, 'rb') as filein:
			while True:
				i = i+1
				line_list = filein.readline().decode('UTF-8')
				if line_list:
					#try:
					j = j+1
					line_list = line_list.replace('\u2022', '')
					line_list = line_list.replace('\u25aa', '')
					line_list = line_list.replace('', '')
					line_list = line_list.replace('\u30fb', '')
					
					line_list = line_list.strip('\n').split(';')
					writer.writerow(line_list[0:])
					#catch(Exception e):

				else:
					break

print("OK!!!!!!!!!")
print(j)
