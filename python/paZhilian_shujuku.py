#!/usr/bin/python
#-*-coding:utf8-*-
# import requests       #urllib2   urllib3   httpclint
# import re             #bs4  xpath
# import json
# def requ_zhilian():
#     #获取网址
#     url = 'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=530&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E6%B5%8B%E8%AF%95%E5%B7%A5%E7%A8%8B%E5%B8%88&kt=3&_v=0.80227393&x-zp-page-request-id=f87af125666b430e9d4d58ebca7e11a2-1572693692073-421812&x-zp-client-id=56829ca5-429c-4047-8e48-534f35e5ac20'
#     requ = requests.get(url)
#     html = requ.json()
#     return html
# def create_database():
#     import pymysql
#     connect = pymysql.connect(host='192.168.10.98', user='root', password='123456', port=3306)
#     cusor = connect.cursor()
#     cusor.execute('create database zlzp;')
#     connect.commit()
#     cusor.close()
# def rd_json(shuJu,i):
#     jobName = shuJu['data']['results'][i]['jobName']
#     company = shuJu['data']['results'][i]['company']['name']
#     salary = shuJu['data']['results'][i]['salary']
#     city = shuJu['data']['results'][i]['city']['display']
#     return city,company,jobName,salary
# def addTo_database(html,nums):
#     import pymysql
#     connect = pymysql.connect(host='192.168.10.98', user='root', password='123456', port=3306)   #后面可加database='数据库名称'  charset='utf-8'
#     cusor = connect.cursor()
#     cusor.execute('use zlzp;')
#     cusor.execute('create table zl(city char(80),company char(80),jobName char(80),salary char(80));')
#     for i in range(nums):
#         cusor.execute('insert into zl values("{}","{}","{}","{}");'.format((rd_json(html,i)[0]),(rd_json(html,i)[1]),(rd_json(html,i)[2]),(rd_json(html,i)[3])))
#     connect.commit()
#     cusor.close()
# import time
# html=requ_zhilian()
# time.sleep(3)
# time.sleep(1)
# addTo_database(html,5)


import requests   #  urllib2  urllib3   httpclient
import re         #  bs4   xpath
import pymysql

class Zhi_L(object):
    def qingqiu(self,page):
        url = 'https://fe-api.zhaopin.com/c/i/sou?start={}&pageSize=90&cityId=765&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95%E5%B7%A5%E7%A8%8B%E5%B8%88&kt=3&_v=0.86522508&x-zp-page-request-id=ba4169b228c54afab493b28e933d6fde-1573196958794-101796&x-zp-client-id=dadd826c-8aad-4163-a64d-59cb72ebc44b&MmEwMD=4l7ytyAyeM34my_lcbYNg1_RjRrkSo2AF_4EXGQHKI0aSgP_RbDUZ8aIDPRzYfl.wh63a9MV.zBbEsECH1WeUOKDMAt9HRcVkboxEKbyM.8bdGEnqldYKnaq60hhNtdaWm5qqekgngzUDqYByikFotq6iN7DGx.gg4Ug6HQbHqdI_6x4FL1BMciZ7fcQb1CGkQ8qYn7IOJJWngkb673KtkkBJ.z1Yn9ZZldCFBxkVxzihUO7i8fGWm4K9a5hMlcIJ5RGhfVxoxk535VclwtqDe_MX_Ai._Fb6tbt..u7C8uIbFg_WdPvsY.Cq7Ez7vwFno5Kc0FjqPDiz9_Hp1UFWs8apC39ut4q.847EPnyzCmYJjeNqqx4BLuhcXAvlOUvV8C0YKB9Itr9_ttYtMPdU52LTHqfwIiXa0_EIKf11d43LdKIlJDjU2ZS3a5ywmnzqSjv'.format(page)
        res = requests.get(url)
        html = res.json()
        return html

    def guo_lv(self,html):
        name,xinzi = [],[]
        for i in range(90):
            name_1 = html['data']['results'][i]['company']['name']
            xinzi_1 = html['data']['results'][i]['salary']
            name.append(name_1)
            xinzi.append(xinzi_1)
        shuju = dict(zip(name,xinzi))
        return shuju

    def save_shuju(self,shuju):
        conn = pymysql.connect(host='192.168.10.98',port=3306,user='root',password='123456')
        su = conn.cursor()
        try:
            su.execute('create database zhilian;')
            su.execute('use zhilian;')
            su.execute('create table zhilian(name char(80),xinzi char(50));')
            for i,j in shuju.items():
                su.execute('insert into zhilian values("{}","{}");'.format(i,j))
                conn.commit()
        except:
            su.execute('use zhilian;')
            for i,j in shuju.items():
                su.execute('insert into zhilian values("{}","{}");'.format(i,j))
                conn.commit()
        finally:
            conn.close()

aa = Zhi_L()
for q in range(0,181,90):
    html = aa.qingqiu(q)
    shuju = aa.guo_lv(html)
    aa.save_shuju(shuju)