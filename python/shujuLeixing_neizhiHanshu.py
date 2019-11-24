#!/usr/bin/python
#-*-coding:utf8-*-
'''切片'''
#将下标号放在冒号前面，显示从下标号开始显示
# a = "abcdefg"
# print(a[-2:])

#将下标号放在冒号后面，显示从开始到下标位置前一位
# a = "hjsbabx"
# print(a[:-5])

# #将两者结合,从冒号前数字开始，到后面数字前的一位
# a = "aksjhdk"
# print(a[2:6])

#将下标号放在两个冒号前，显示从下标号对应的字符开始到结尾
# a = "dgahxjkl"
# print(a[3::])
#放在两个冒号后，以此数字分组，显示组内第一个,-1为倒叙
# print(a[::-3])
#两者结合，从前面数字的下标位置开始以后面数字分组，显示组内第一个
# print(a[1::3])

'''1.字符串'''
'''1.upper():将小写变大写'''
# a = "asgk".upper()
# print(a)
'''2.lower():将大写变小写'''
# a = "SJAGJ".lower()
# print(a)
# print(input("请输入一串小写字符").lower())
'''3.将首字母大写'''
# a = input("请输入一串小写字符")
# b = a.title()
# print(b)
'''4.swapcase():大小写相互转换'''
# a = input("请输入一串小写字符")
# b = a.swapcase()
# print(b)
'''5.replace(“原内容”，“替换内容”，替换数量)：将字符串中的字符替换为其他数据'''
# a = "1254115"
# b = a.replace("1","a",2)
# print(b)
'''6.split(‘分隔符’):以括号中的数据为分隔符，将字符串分割成列表'''
# a = "2125416815"
# b = a.split("1")
# print(b)
'''7. 分隔符.join(元素序列)：以某个数据将列表中的元素连接起来形成新的字符串'''
# print("-".join("gjhdasc"))
# a = ["gdk","hcaks"]
# b = "-".join(a)
# print(b)

# c = "uluajkdhkajjkaiop"
# a = c.split("a")
# b = "-".join(a)
# print(b)

'''8.startswith(‘字符串’)：判断是否以括号中的字符开头'''
# a = 'hclsajcl'.startswith("h")
# print(a)
'''9.endswith(‘字符串’)：判断是否以括号中字符串的结尾'''
# a = 'hclsajcl'.endswith("l")
# print(a)

'''10.字符串格式化的三种格式'''

'''1.“%” % 填的字符 %s:通过str()将输入的字符转化为字符串 %d:只能填整数
 %f:只能填浮点数'''
# b = 123
# a = "%d" % b
# print(a)
'''2."{}".format():格式化字符串'''
# a = "{}*{}={}".format(1.1, 2, 1.1*2)
# print(a)
'''3.f"{}"'''
# a="ukshxckas"
# b="12536531383"
# print(f"{a}{b}{a}")

'''11.strip():去除字符串左右两边的字符串 只去除左边lstrip,右边rstrip 只有一边和括号中一样，就去除
一样的那边'''
# b = "hwah".strip("h")
# print(b)
# i = "qwerhkhuewqq"
# b = i.strip("qwer")
# print(b)
'''12.count():统计字符串的数量'''
# b = "dhuidlkdjildj".count("d")
# print(b)
'''13.index():括号中字符串所在的下标 括号内可以加区间，如果不加就是默认从下标为0开始的第一个括号中的字符
的下标  如果字符后直接写一个数字，就表示显示从下标为那个数字开始的第一个括号内的字符的下标'''
# b = "hgkjpxgaohcisoyciuihisagi".index("g",2)
# print(b)
'''14.len():统计有多少个元素'''
# b = "dhoisa"
# print(len(b))

'''2.列表'''


'''字典    dict'''
# a = {'name':'zhangsan',
#      'age':18,
#      'sex':'nan',
#      '1':[1,2,3]}
# a.popitem()    #默认删除最后一个
# a.pop('name')  #根据键来删除数据
#print(a.keys())  #获取所有的key
#print(a.values())  #获取所有的值
#print(a.items())  #获取所有的键值对
# b = {'aaa':'akh'}
# a.update(b)      #将字典b的数据追加到字典a里面
# print(a)
