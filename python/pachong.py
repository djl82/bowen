#!/usr/bin/python
#-*-coding:utf8-*-
# import re
# a='wqe\nQfwq123qfQwqw'
# #匹配（wq）这一组数据
# zhengZe=re.compile('(wq)')   #('wq',re.S)输出一样
# result=re.findall(zhengZe,a)
# #匹配以q到q之间的数据，换行符不能匹配
# zhengZe1=re.compile('q(.*)q')
# result1=re.findall(zhengZe1,a)
# #可以匹配换行符   正则表达式后面加re.S
# zhengZe2=re.compile('q(.*)q',re.S)
# result2=re.findall(zhengZe2,a)
# print(result,result1,result2)
# #不区分大小写
# zhengZe3=re.compile('q(.*)q',re.I)
# result3=re.findall(zhengZe3,a)
# print(result3)
# #非贪婪模式   尽可能取少，不重复使用字符
# '''1.*?:匹配0次
# 2.+?:匹配1次
# 3.??:匹配0次
# 4.{M,N}?:匹配M次'''
# zhengZe4=re.compile('q(.*?)q',re.I)
# result4=re.findall(zhengZe4,a)
# print(result4)


# import requests
# import re
# url = 'http://www.quanshuwang.com/book/9/9055/9674264.html'
# #请求网页
# html=requests.get(url)
# #接收响应内容的  网页是用什么样的编码写的就用相应的编码方式解码
# neiRong=html.content.decode('GBK')
# # print(neiRong)
# zhengZe=re.compile('</script>&nbsp;(.*?)<script type="text/javascript">style6',re.S)
# result=re.findall(zhengZe,neiRong)
# a='&nbsp;'+result[0]+'<br />'
# jieguo=re.findall(re.compile('&nbsp;&nbsp;&nbsp;&nbsp;(.*?)<br />',re.S),a)
# txt=open(r'c:\Users\ding\Desktop\2.txt','w',encoding='utf8')
# for i in jieguo:
#     txt.write(i+'\n\n')
# txt.close()

# import requests
# import json
# url = 'https://www.amap.com/service/poiInfo?query_type=TQUERY&pagesize=20&pagenum=1&qii=true&cluster_state=5&need_utd=true&utd_sceneid=1000&div=PC1000&addr_poi_merge=true&is_classify=true&zoom=12&city=410200&geoobj=114.290626%7C34.72929%7C114.653215%7C34.819543&keywords=%E5%BC%80%E5%B0%81%E5%A4%A7%E5%AD%A6'
# #简单反爬机制
# head = {'Host':'www.amap.com',
# 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0',
# 'Accept':'*/*',
# 'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
# 'Accept-Encoding':'gzip, deflate, br',
# 'amapuuid':'ca695ec8-efb8-4873-97aa-ad6313af6938',
# 'x-csrf-token':'null',
# 'X-Requested-With':'XMLHttpRequest',
# 'Connection':'keep-alive',
# 'Referer':'https://www.amap.com/place/B017A0N1XL',
# 'Cookie':'guid=63a3-bdbe-4246-a224; key=bfe31f4e0fb231d29e1d3ce951e2c780; UM_distinctid=16e24881123293-0c04977acab5cb-4c302b7a-144000-16e248811241f5; CNZZDATA1255626299=2102828773-1572567107-https%253A%252F%252Fwww.baidu.com%252F%7C1572567107; cna=EUUFFh0anToCAbZ+/MOZRv8k; isg=BFlbK_VcYHNitTznbI7EWa5la0XzTke_RRRB73suygC6gkMUPzdcaOHUhIZRIeXQ; l=dBxdl4muqlCNRNAXBOfNNuIRh1QO0sAqkkPzw4wM2IBGGEwDRAxH9rlYd4up4V7pAbghnsdnG34ItnNmIe4p2R2Zh-qPAKsyitNnndLh.; _uab_collina=157257092977209873315626'}
# html = requests.get(url,headers=head)
# result = html.text
# #将json格式转换为字典格式
# result = json.loads(result)
# for i in range(20):
#     print(result['data']['poi_list'][i]['name'])
