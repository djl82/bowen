#!/usr/bin/python
#-*-coding:utf8-*-
import pymysql
#192.168.10.98
#连接mysql，host：mysql数据库所在的主机地址
#user：mysql数据库用户名
#password：mysql用户密码
#port：mysql端口号
connect = pymysql.connect(host = '192.168.10.98',user = 'root', password = '123456', port = 3306)
#创建游标，一种临时的数据库对象，相当于购物车
cusor = connect.cursor()
#创建数据库
# cusor.execute('create database dji')
#使用这个数据库
cusor.execute('use dji;')
#创建表
# cusor.execute('create table stu(name char(50),age int);')
# #添加数据
# cusor.execute('insert into stu values("丁金玲","21");')
cusor.execute('select * from stu;')
# #取出表中的一行数据，可迭代
# data = cusor.fetchone()
# print(data)
#取出表中所有数据，以元组表示
# data = cusor.fetchall()
# print(data)
#默认取出一个，传参几就取出几个，数字大于数据总数,就只取出所有数据，可迭代
data_1 = cusor.fetchmany()
print(data_1)

#数据库提交数据，在插入数据的时候一定要提交，否则提交的数据就不会被保存在数据库中，只会保存在临时数据库中
connect.commit()
connect.close()