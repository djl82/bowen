#!/usr/bin/python
#-*-coding:utf8-*-

# import requests
# import re
# for wangzhi in range(264,703):
#     url = (f'http://www.quanshuwang.com/book/9/9055/9674{wangzhi}.html')
#     #请求网页
#     html=requests.get(url)
#     #接收响应内容的  网页是用什么样的编码写的就用相应的编码方式解码
#     neiRong=html.content.decode('GBK')
#     # print(neiRong)
#     biaoti = re.findall(re.compile('<title>盗墓笔记_(.*?)_全书网</title>',re.S),neiRong)
#     zhengZe=re.compile('<div class="mainContenr"(.*?)<script type="text/javascript">style6',re.S)
#     result=re.findall(zhengZe,neiRong)
#     a=(result[0]+'<br />')
#     jieguo=re.findall(re.compile('&nbsp;&nbsp;&nbsp;&nbsp;(.*?)<br />',re.S),a)
#     with open(r'c:\Users\ding\Desktop\2.txt','a',encoding='utf8') as f:
#         f.write('\t\t\t\t\t\t'+biaoti[0]+'\n')
#         for i in jieguo:
#             f.write(i+'\n\n')


# import requests
# import re
# #用来请求网页的
# for dz in range(1,11):
#     request_html = requests.get(f'http://www.mmonly.cc/sgtp/list_1_{dz}.html')
#     #用来接收响应的以及设置接收的编码方式
#     reponse = request_html.content.decode('gbk')
#     #正则表达式预编译
#     regular = re.compile('<div class="img">(.*?)original="',re.S)
#     #编译匹配响应内容
#     filtrate = re.findall(regular,reponse)
#     wenZi = re.findall(re.compile('alt="(.*?)"',re.S),str(filtrate))
#     tuPian = re.findall(re.compile('src="(.*?)"',re.S),str(filtrate))
#     for i,j in zip(wenZi,tuPian):
#         #通过链接请求图片
#         request_picture = requests.get(j)
#         #接收请求的字节码
#         picture = request_picture.content
#         print(picture)
#         #将字节码编成图片存储到文件夹里
#         with open(r'c:\Users\ding\Desktop\tp\{}.jpg'.format(i),'wb') as f:
#             f.write(picture)

# import requests
# import re
# for dz in range(1,6):
#     request_html = requests.get(f'http://www.mmonly.cc/sgtp/list_1_{dz}.html')
#     reponse = request_html.content.decode('gbk')
#     regular = re.compile('<div class="img">(.*?)original="',re.S)
#     filtrate = re.findall(regular,reponse)
#     wenZi = re.findall(re.compile('alt="(.*?)"',re.S),str(filtrate))
#     tuPian = re.findall(re.compile('src="(.*?)"',re.S),str(filtrate))
#     for i,j in zip(wenZi,tuPian):
#         request_picture = requests.get(j)
#         picture = request_picture.content
#         print(picture)
#         with open(r'c:\Users\ding\Desktop\tp\{}.jpg'.format(i),'wb') as f:
#             f.write(picture)

# import requests
# import re
# for i in range(79609,80350):
#     url = (f'http://www.quanshuwang.com/book/44/44683/153{i}.html')
#     html = requests.get(url)
#     neiRong = html.content.decode('gb18030')
#     # biaoTi = re.findall(re.compile('<title>斗罗大陆_(.*?)(全书完)_全书网</title>',re.S),neiRong)
#     guoLv = re.findall(re.compile('</script>&nbsp;(.*?)<script type="text/javascript">style6',re.S),neiRong)
#     guoLv = '&nbsp;' + str(guoLv)
#     jieGuo = re.findall(re.compile('&nbsp;&nbsp;&nbsp;&nbsp;(.*?)<br />',re.S),guoLv)
#     with open(r'c:\Users\ding\Desktop\douluodalu.txt','a',encoding='utf-8') as f:
#         for j in jieGuo:
#             f.write(j)
#             f.write('\n')