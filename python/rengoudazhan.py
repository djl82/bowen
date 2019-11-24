#!/usr/bin/python
#-*-coding:utf8-*-
class People():
    def __init__(self,name):
        #玩家姓名
        self.name=name
        #玩家血量
        self.xueLiang=100
        #玩家攻击力
        self.gongJiLi=5
        self.gouXueLiang = 1
    def __str__(self):   #为了显示的更好看一点
        wanjia = "-"*30+'\n'
        wanjia += '玩家：'+self.name+'\n'
        wanjia += '血量：'+str(self.xueLiang)+'\n'
        wanjia += '攻击力：'+str(self.gongJiLi)+'\n'
        if self.gouXueLiang==0:
            wanjia+='狗死了，玩家赢了'
        return wanjia
    def attack(self,gou):
        if gou.xueLiang>0:
            gou.xueLiang-=self.gongJiLi
        self.gouXueLiang=gou.xueLiang
class Dog():
    def __init__(self,name):
        #狗命
        self.name=name
        #狗命
        self.xueLiang = 100
        #狗力
        self.gongJiLi = 5
        self.wanjiaXueLiang=1
    def __str__(self):
        gou = "-"*30+'\n'
        gou += '狗名：'+self.name+'\n'
        gou += '狗命：'+str(self.xueLiang)+'\n'
        gou += '狗力：'+str(self.gongJiLi)+'\n'
        if self.wanjiaXueLiang==0:
            gou +='人死了，狗赢了'
        return gou
    def gouJi(self,wanjia):
        if self.xueLiang > 30:
            wanjia.xueLiang -= (self.gongJiLi)*2
        if wanjia.xueLiang>0:
            wanjia.xueLiang-=self.gongJiLi
        self.wanjiaXueLiang=wanjia.xueLiang

p1=People('Tom')
print(p1)
p2=People('JieRui')

g1=Dog('赤血狂犬')
print(g1)

while 1:
    p1.attack(g1)
    p2.attack(g1)
    g1.gouJi(p1)
    if g1.xueLiang==0 or p1.xueLiang==0 or p2.xueLiang==0:
        break
print(g1)
print(p1,p2)