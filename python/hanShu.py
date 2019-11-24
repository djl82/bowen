#!/usr/bin/python
#-*-coding:utf8-*-
'''enumerate'''
#当某个函数运行的结果有多个时可以用多个变量来接收
# a = ['qwe', 'dhilsa', 'hcli']
# for i,j in enumerate(a):
#     print(i,j)

# li = ['手机', '电脑', '鼠标垫', '游艇']
# for i,j in enumerate(li):
#     print(i,j)
# b = int(input("请输入所要选择商品的序号："))
# print(li[b])

'''列表推导式'''
# 列表推导式：将条件控制语句写在列表中，产生的结果会自动存储在列表中
# 格式：[语句结果  条件控制语句]
# 10以内偶数的平方
# a = []
# for i in range(2,11,2):
#     a.append(i ** 2)
# print(a)
#
# b = [i**2 for i in range(2,11,2)]
# print(b)

# 函数：具有某种功能的，可重复使用的代码块
# 节省代码，可以重复使用
# 格式：def 函数名（）：
#            执行语句
# 函数名的命名规则和变量名的规则一样

'''1.
def feng7guo():
    for a in range(100):
        if a % 7 == 0 or a // 10 == 7 or a % 10 == 7:
            print(a, end="\t")


feng7guo()
'''

'''2.变量的作用域    局部变量和全局变量
局域变量：只在函数内有用的变量
（只在一小块区域内有用）
全局变量：在整个py文件中都可以使用的
（在任何区域都能使用的）
a = 4
def aaa():
    global a   #global   将局域变量转化为全局变量
    a = 2
    print(a)
aaa()
print(a)'''

'''3.参数传递
3.1   必须参数   必须填写的参数
参数名的规则和变量名的规则一样
格式  def 函数名（参数名）：
             执行语句
def sum1(x):
    b = sum(range(x + 1))
    print(b) 
sum1(123)     #(0+1+2+……+121+122)

3.2  默认参数  当调用函数时传入数据了就使用传入的数据，如果不传入数据就使用默认值
格式  def 函数名（参数名=值）：
               执行语句
def sum1(x=2,y=100):
    a = 0
    for i in range(x,y+1):
        b = [j for j in range(2,i) if i%j==0]
        if len(b)==0:
            a += i
    print(a)
sum1(50,100)

3.3  可变长参数   一次性可接受多个数据  接收到的数据是个元组，特性跟默认参数一样，可传可不传
格式  def 函数名（*参数名）：
            执行语句
def sum1(*args):       #*args为Python默认写法
    print(args)
sum1([12,154],'gcskja',153)

3.4   关键字参数：传入的数据必须是键值对格式，接受到的数据类型是字典
格式  def 函数名（**参数名）：
            执行语句
def sum1(**kwargs):       #**kwargs为Python默认写法
    print(kwargs)
sum1(name=123,sgau=4586)

优先级：必须参数 > 默认参数 > 可变长参数

4.return   返回值
作用：1.将return后面的数据赋值给函数的调用者
      2.结束函数
格式    def 函数名（）：
             执行语句块
             return 数据（注：数据的个数根据实际情况而定）

计算0到人和数之间的和
计算2到sum结果之间因数的和等于本身的数
def sum1(x):
    b = sum(range(x + 1))
    return b
def sum2(x):
    for i in range(2,x + 1):
        b = [j for j in range(1,i) if i % j == 0]
        if sum(b)==i:
            print(i)
c = sum1(50)
print(c)'''

# 输入a和b两个数据，a为列表，b为数字，当列表a中的两个数字和为b时，输出那两个数字
# def sz(a=[],b=0):
# #     for i in range(len(a)-1):
# #         for j in range(i+1,len(a)):
# #             if a[i] + a[j] == b:
# #                 print(a[i],a[j])
# # sz([12,11,5,2,3,10,4],14)

# def hanshu():
#     def hanshu1(x,y):
#         a=x+y
#         print(a)
#     return hanshu1
# a=hanshu()#这时候函数hanshu（）并没有执行，而是指向一个求和的函数位置只有调用a()才会执行
# a(1,2)

'''异常处理'''
# try:
#     print('执行了try语句')
#     b = '123'
#     int(b)
# except Exception as b:
#     print(b,'执行了except语句')
# else:
#     print('执行了else语句')
# finally:
#     print('执行了finally语句')

# try :
#     a = 'adhskj'
#     int(a)
#     raise   TypeError('这是类型错误')
# except Exception as e:
#     print(e)

# try:
#     a=33
#     print(a+'12')
# except Exception as e:
#     print(e)
# try:
#     a=33
#     print(a+'12')
# except NameError as e:
#     print(e)
# except TypeError as e:
#     print(e)

'''类'''
#类名首字母大写
#创建一个类
#类分两种   第一种是经典类 class Dog:  第二种是新式类 class Dog(object):
'''class Dog:  #类名，类的抽象
    #属性
    #方法
    def run(self):
        print('-----跑-----')
        self.pee()
    def pee(self):
        print('-----撒尿-----')
        print(self.color)
    def info(self):
        self.pee()
        print(self.color)
        print(self.name)
        print(self.weiba)
        print(self.sex)
        print(self.tuiCount)
#创建一个叫大狗的对象
bigDog=Dog()   #类的实例
bigDog.name='大黄狗'
bigDog.color='黄色'
bigDog.weiba='有'
bigDog.sex='公'
bigDog.tuiCount='3'
# print(bigDog.name)
# print(bigDog.color)
# print(bigDog.weiba)
# print(bigDog.sex)
bigDog.info()
bigDog.run()
bigDog.pee()
#创建一个叫黄狗的对象
huangDog=Dog()
huangDog.name='黄狗'
huangDog.color='黄色'
huangDog.weiba='没有'
huangDog.sex='母'
huangDog.tuiCount='4'
# print(huangDog.name)
# print(huangDog.color)
# print(huangDog.weiba)
# print(huangDog.sex)
huangDog.info()
huangDog.run()
huangDog.pee()'''

# class Lei:
#     a = 'hanshu'
#     def hanshu111(self):
#         print('123')
#     def hanshu(self):
#         print(self.a)
#         self.hanshu111()
# class Dog:
#     def call(self):
#         print('----汪汪----')
# class NewLei(Lei,Dog):
#     pass
# xiaoming=NewLei()
# xiaoming.hanshu111()
# xiaoming.hanshu()
# xiaoming.call()
# class Xiaoxiao(NewLei):
#     def aaa(self):
#         self.hanshu()
# b=Xiaoxiao()
# b.aaa()

# import abc
# class Animal(metaclass=abc.ABCMeta):  #同一类事物：动物
#     @abc.abstractclassmethod
#     def talk(self):
#         pass
# class People(Animal):
#     def talk(self):
#         print('hello world!')
# class Pig(Animal):
#     def talk(self):
#         print('hengheng')
# class Dog(Animal):
#     def talk(self):
#         print('wangwang')
# def aaa(obj):    #定制一个统一的接口，不需要考虑实例的类型
#     obj.talk()
# aaa(People())

# class Dog():
#     def __init__(self,color,weiba):
#         self.color=color
#         self.weiba=weiba
#         print(self.color)
#         print(self.weiba)
#     def pee(self):
#         print('--撒尿--')
# huangDog=Dog('黄色','有尾巴')
# huangDog.pee()
# gou=Dog('黑色','尾巴咬断了')