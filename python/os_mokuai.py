#!/usr/bin/python
#-*-coding:utf8-*-
#不限制平台，os本意就是操作系统
import os
# 查看操作系统
# print(os.name)
# #显示当前路径
# a = os.getcwd()
# print(a)
#删除文件
# delete = os.remove('a.txt')
#只能删除空目录
# delete_dir = os.removedirs('111')
#返回指定路径下所有的文件和目录名，括号内填相对路径或绝对路径    ‘.’：代表当前路径   ‘..’：代表上一级
# list = os.listdir('.')
# print(list)
# for i in list:
#     if i.endswith('.xls'):
#         os.remove(i)
# #创建单级目录
# dir = os.mkdir('qqq')
# #创建递归目录
# dirs = os .makedirs(r'qqq\111\222\333')
# #删除递归目录，都要是空目录
# delete_dir = os.removedirs(r'qqq\111\222\333')
# #删除单级目录
# delete_dir = os.rmdir('qqq')
#指定路径下的名称是不是文件
a = os .path.isfile('b.txt')
print(a)
#判断指定目录下文件是不是目录
b = os.path.isdir('b.txt')
print(b)
#判断文件或目录是否存在
bb = os.path.exists('b.txt')
print(bb)
#将路径分割成路径名和文件名
c = os.path.split(r'D:\python\b.txt')
print(c)
#链接目录与文件名或目录
cc = os.path.join('D:\\python', 'b.txt')
print(cc)
