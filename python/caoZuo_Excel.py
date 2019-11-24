#!/usr/bin/python
#-*-coding:utf8-*-

# import xlwt
# geshi=xlwt.Workbook(encoding='utf-8')    #写入Excel文件的格式
# #创建标签页，并命名标签页     cell_overwrite_ok=True表示重设值
# sheet=geshi.add_sheet('py-1906',cell_overwrite_ok=True)
# sheet1=geshi.add_sheet('123')
# #往标签页里写入内容，第一个表示行，第二个表示列，第三个表示写入的内容
# #会将文件清空
# sheet.write(0,0,'内容')
# # for i in range(9):
# #     for j in range(i+1):
# #         sheet.write(i,j,'%d*%d=%d' %((i+1),(j+1),(i+1)*(j+1)))
# # 创建一个或多个Excel文件
# geshi.save('我的Excel.xls')



# import xlwt
# geshi=xlwt.Workbook(encoding='utf-8')
# sheet=geshi.add_sheet('py-1906')

# txt=open('a.txt','r',encoding='utf8')
# a=txt.readlines()
# txt.close()
# print(a)
# b = []
# for i in range(len(a)):
#     b = a[i].replace('\n','\t').split('\t')
#     for j in range(len(b)):
#         sheet.write(i,j,b[j])

# geshi.save('zhuanhuan.xls')

# import xlwt
# geshi=xlwt.Workbook(encoding='utf-8')
# sheet=geshi.add_sheet('123')
# i=open('a.txt','r',encoding='utf-8')
# a = i.readlines()
# i.close()
# for j in range(len(a)):
#     sheet.write(j,0,a[j])
# geshi.save('456.xls')

# import xlrd
# wenjian = xlrd.open_workbook('456.xls')
# '''第一种方法进入标签页'''
# # #有多少个标签页
# # a = wenjian.nsheets
# # #通过索引值进入标签页
# # b = wenjian.sheets()[0]
# # #获取第一个格子里的值
# # gezi = b.cell(0,0).value
# # print(gezi)
# '''第二种方法进入标签页'''
# #获取文件中所有标签页的名称
# a = wenjian.sheet_names()
# #通过标签页名进入到标签页
# b = wenjian.sheet_by_name('123')
# #获取标签页中内容有多少行
# hang = b.nrows
# print(hang)
# #以列表的形式显示一行内容
# for i in range(hang):
#     hang_neiRong=b.row_values(i)[0]
#     print(hang_neiRong)
# #获取标签页格子里的内容
# for i in range(10):
#     gezi = b.cell(i,0).value
#     print(gezi);[[r
#获取标签页中总共有多少列
# lie=b.ncols
# print(lie)
# lie_neirong=b.col_values(0)
# print(lie_neirong)

# from xlutils.copy import copy
# import xlrd
# file=xlrd.open_workbook('456.xls')
# #不是直接操作我们打开的excel文件，而是复制一份操作复制的文件，只有写的操作，没有读的操作
# New_file=copy(file)
# #get_sheet(下标位置)，根据下标位置进入标签页
# sheet=New_file.get_sheet(0)
# sheet.write(9,9,'neirong')
# New_file.save('789.xls')

# import xlwt
# geshi=xlwt.Workbook(encoding='utf-8')
# sheet=geshi.add_sheet('123')
# i=open('a.txt','r',encoding='utf-8')
# a = i.readlines()
# i.close()
# for j in range(len(a)):
#     c = a[j].split('\t')
#     for b in range(len(c)):
#         sheet.write(j,b,c[b])
# geshi.save('456.xls')

# import xlrd
# wenjian = xlrd.open_workbook('456.xls')
# a = wenjian.sheets()[0]
# l = []
# for i in range(9):
#     lie = a.ncols
#     k = []
#     for j in range(lie):
#         k.append(a.cell(i,j).value)
#     while 1:
#         if k.count('') > 0:
#             k.remove('')
#         else:
#             break
#     l.append(k)
# txt=open('a.txt','w',encoding='utf8')
# for p in l:
#     p = '\t'.join(p)
#     txt.write(p)
# txt.close()

# import xlrd
# wenjian = xlrd.open_workbook('456.xls')
# b = wenjian.sheets()[0]
# aa = []
# for i in range(b.nrows):
#     for j in range(b.ncols):
#         aa.append(b.cell(i,j).value)
# with open('b.txt','w',encoding='utf-8') as f:
#     for q in aa:
#         if q == '':
#             continue
#         elif q == '\n':
#             f.write(q)
#         else:
#             f.write(q+'\t')
