#!/usr/bin/python
#-*-coding:utf8-*-
# txt=open('a.txt','w',encoding='utf8')
# for i in range(1,10):
#     for a in range(1,i+1):
#         txt.write(f'{a}*{i}={a*i}\t')
#     txt.write('\n')
# txt.close()

# txt=open('a.txt','w',encoding='utf8')
# q = int(input("多少行："))
# for a in range(q):
#     if a <= ((q-1)//2):
#         txt.write('\t'*((q-1)//2-a))
#         txt.write('1234\t'*(a + 1))
#         txt.write("\n")
#     else:
#         txt.write('\t' * (a-(q-1)//2))
#         txt.write('1234\t' * (q - a))
#         txt.write("\n")
# txt.close()

# txt=open(r'D:\python\123.py','r',encoding='utf8')
# a = txt.read()
# print(a)
# txt.close()

# txt=open('a.txt','r',encoding='utf8')
# while True:
#     c = txt.readline()
#     print(c)
#     if c == '\n':
#         break
# txt.close()

# txt=open('a.txt','r',encoding='utf8')
# c = txt.readlines()
# print(c)
# txt.close()

# a=open('for循环.py','r',encoding='utf8')
# c = a.readlines()
# print(c)
# a.close()

# a=open('for循环.py','r',encoding='utf8')
# i = 0
# j = 0
# while 1:
#     c = a.readline()
#     if c.startswith('#'):
#         i += 1
#     elif c == '\n':
#         j += 1
#     elif c == '':
#         break
# print(i,j)
# a.close()

#追加
# txt=open('a.txt','a',encoding='utf-8')
# txt.write('\nxkljaslkc')
# txt.close()

#读和写的权限
# txt=open('a.txt','r+',encoding='utf-8')
# txt.write('\nxkljaslkc')
# print(txt.readlines())
# txt.close()
#不写编码方式就默认ANSI

# a=open(r'c:\Users\ding\Desktop\2b525660faea9ea6.gif','rb')
# b = a.read()
# a.close()
# print(b)
# c = open('00.gif','wb')
# c.write(b)
# c.close()

# with open('a.txt','r') as f:
#     print(f.read())

# a = open('a.txt','r',encoding='utf-8')
# b = a.readlines()
# for i in b:
#     if i.count('abc') >= 1:
#         print(i)
# a.close()

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