#!/usr/bin/python
#-*-coding:utf8-*-
# import time
# # second=time.time()
# # print(second)
# # #显示的是本地时间
# shijian=time.localtime()
# print(shijian)
# # #显示的utc时间
# # utc_shijian=time.gmtime()
# # print(utc_shijian)
#
# a = time.strftime('%y-%m-%d %H:%M:%S:%w', time.localtime())
# print(a)

# import time
# geShiHua=time.strftime('%Y-%m-%d-%W-%w %X',time.localtime())
# print(geShiHua)
# shiJian=time.strptime('2019-10-29-43-2 09:49:47','%Y-%m-%d-%W-%w %X')

# import time
# jieGouhua=time.strptime('2019/10/28 18:00:00','%Y/%m/%d %X')
# shiJian=time.mktime(jieGouhua)
# xianShijian=time.time()
# print(xianShijian-shiJian)

# from time import *

# nian=int(input('请输入一个年份：'))
# if nian % 100 == 0:
#     if nian % 4 == 0:
#         print('闰年')
#     else:
#         print('平年')
# else:
#     if nian % 4 == 0:
#         print('闰年')
#     else:
#         print('平年')