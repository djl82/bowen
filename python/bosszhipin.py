#!/usr/bin/python
#-*-coding:utf8-*-
import requests
import re
import json
import time

def request_zhilian():
    #获取网址
    url = 'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=530&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E6%B5%8B%E8%AF%95%E5%B7%A5%E7%A8%8B%E5%B8%88&kt=3&_v=0.05730650&x-zp-page-request-id=23b27437912f404a919d80bda462c28b-1572600523270-416219&x-zp-client-id=56829ca5-429c-4047-8e48-534f35e5ac20'
    #简单的防爬
    head = {'Host':'fe-api.zhaopin.com',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0',
'Accept':'application/json, text/plain, */*',
'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
'Accept-Encoding':'gzip, deflate, br',
'Origin':'https://sou.zhaopin.com',
'Connection':'keep-alive',
'Referer':'https://sou.zhaopin.com/?jl=530&kw=%E6%B5%8B%E8%AF%95%E5%B7%A5%E7%A8%8B%E5%B8%88&kt=3',
'Cookie':'urlfrom2=121113803; adfcid2=pz_bg_beijingzhiwei; adfbid2=0; x-zp-client-id=56829ca5-429c-4047-8e48-534f35e5ac20; sts_deviceid=16db0c8e001a-0c8b25243f5e038-4c312373-1327104-16db0c8e003392; acw_tc=2760825115706290176814609e4fff742f4b3625ab8962359582aff4a44321; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216db0c8e044126-07e3d75de8f5c58-4c312373-1327104-16db0c8e045a%22%2C%22%24device_id%22%3A%2216db0c8e044126-07e3d75de8f5c58-4c312373-1327104-16db0c8e045a%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E4%BB%98%E8%B4%B9%E5%B9%BF%E5%91%8A%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fsp0.baidu.com%2F9q9JcDHa2gU2pMbgoY3K%2Fadrc.php%3Ft%3D06KL00c00fZmx9C0jZ7-0KqiAsKcSUVI00000rbOfNC00000VM6z7M.THLyktAJdIjA80K85ydEUhkGUhNxndqbusK15H-hrjFWPH99nj0sPym4m1T0IHY1nHNAPDFKnRwjf1fsnHu7fRn1PjI%22%2C%22%24latest_search_keyword%22%3A%22%E6%99%BA%E8%81%94%E6%8B%9B%E8%81%98%22%2C%22%24latest_utm_source%22%3A%22baidupcpz%22%2C%22%24latest_utm_medium%22%3A%22cpt%22%2C%22%24latest_utm_campaign%22%3A%22ty%22%2C%22%24latest_utm_content%22%3A%22tj%22%2C%22%24latest_utm_term%22%3A%2228700043%22%7D%7D; urlfrom=121113803; adfbid=0; sts_sg=1; sts_chnlsid=121113803; zp_src_url=https%3A%2F%2Fsp0.baidu.com%2F9q9JcDHa2gU2pMbgoY3K%2Fadrc.php%3Ft%3D06KL00c00fZmx9C0jZ7-0KqiAsjtvoVI00000P_OfNC00000VM6z7M.THLyktAJdIjA80K85ydEUhkGUhNxndqbusK15ymvPADkuhu-nj0snH7-rHD0IHY1nHNAPDFKnRwjf1fsnHu7fRn1PjIKPjwKnjTYP1TYwfK95gTqFhdWpyfqn1c3rjb4rjc4PiusThqbpyfqnHm0uHdCIZwsT1CEQLILIz4lpA7ETA-8QhPEUHq1pyfqnHcknHD1rj01FMNYUNq1ULNzmvRqmh7GuZNsmLKlFMNYUNqVuywGIyYqmLKY0APzm1Y1PHbdn0%26tpl%3Dtpl_11534_19968_16032%26l%3D1514225627%26attach%3Dlocation%253D%2526linkName%253D%2525E6%2525A0%252587%2525E5%252587%252586%2525E5%2525A4%2525B4%2525E9%252583%2525A8-%2525E6%2525A0%252587%2525E9%2525A2%252598-%2525E4%2525B8%2525BB%2525E6%2525A0%252587%2525E9%2525A2%252598%2526linkText%253D%2525E3%252580%252590%2525E6%252599%2525BA%2525E8%252581%252594%2525E6%25258B%25259B%2525E8%252581%252598%2525E3%252580%252591%2525E5%2525AE%252598%2525E6%252596%2525B9%2525E7%2525BD%252591%2525E7%2525AB%252599%252520%2525E2%252580%252593%252520%2525E5%2525A5%2525BD%2525E5%2525B7%2525A5%2525E4%2525BD%25259C%2525EF%2525BC%25258C%2525E4%2525B8%25258A%2525E6%252599%2525BA%2525E8%252581%252594%2525E6%25258B%25259B%2525E8%252581%252598%2525EF%2525BC%252581%2526xp%253Did(%252522m3288998295_canvas%252522)%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FH2%25255B1%25255D%25252FA%25255B1%25255D%2526linkType%253D%2526checksum%253D64%26ie%3Dutf-8%26f%3D8%26tn%3Dmonline_3_dg%26wd%3D%25E6%2599%25BA%25E8%2581%2594%25E6%258B%259B%25E8%2581%2598%26oq%3D%25E6%2599%25BA%25E8%2581%2594%25E6%258B%259B%25E8%2581%2598%26rqlang%3Dcn; adfcid=pz_bg_beijingzhiwei; dywea=95841923.784168230821045900.1572592401.1572592401.1572592401.1; dywec=95841923; dywez=95841923.1572592401.1.1.dywecsr=baidu|dyweccn=(organic)|dywecmd=organic; Hm_lvt_38ba284938d5eddca645bb5e02a02006=1572592401; Hm_lpvt_38ba284938d5eddca645bb5e02a02006=1572600304; jobRiskWarning=true; __utma=269921210.1275631318.1572592402.1572592402.1572592402.1; __utmc=269921210; __utmz=269921210.1572592402.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; sou_experiment=capi; ZL_REPORT_GLOBAL={%22sou%22:{%22actionid%22:%22f6eb8219-535d-4a0b-86b0-12bcbcfb05f5-sou%22%2C%22funczone%22:%22smart_matching%22}%2C%22company%22:{%22actionid%22:%2296b4f2f7-6541-448e-b049-fb6f67d62ea2-company%22%2C%22funczone%22:%22hiring_jd%22}%2C%22//www%22:{%22seid%22:%22%22%2C%22actionid%22:%220f2dbad6-0b31-400f-ad71-e58150c47915-cityPage%22}}; LastCity=%E5%8C%97%E4%BA%AC; LastCity%5Fid=530; ZP_OLD_FLAG=false; POSSPORTLOGIN=1; CANCELALL=0; sts_evtseq=16; sts_sid=16e2636cc802bc-02fda81fcb25988-4c302b7a-1327104-16e2636cc8179',
'TE':'Trailers'
    }
    #
    requ = requests.get(url, headers=head)
    html = requ.json()      #将json字符串转换为字典，方便以键取值
    return html
# 创建excel
def create_excel():
    import xlwt
    geshi = xlwt.Workbook(encoding='utf-8')
    sheet = geshi.add_sheet('软件测试工程师')
    geshi.save('智联招聘.xls')
def read_json(shuJu,i):
    jobName = shuJu['data']['results'][i]['jobName']
    company = shuJu['data']['results'][i]['company']['name']
    salary = shuJu['data']['results'][i]['salary']
    city = shuJu['data']['results'][i]['city']['display']
    return city,company,jobName,salary
def addTo_excel(html,nums):
    from xlutils.copy import copy
    import xlrd
    read_excel = xlrd.open_workbook('智联招聘.xls')
    new_excel = copy(read_excel)
    sheet_1 = new_excel.get_sheet('软件测试工程师')
    sheet_1.write(0, 0, '城市')
    sheet_1.write(0, 1, '公司')
    sheet_1.write(0, 2, '职位')
    sheet_1.write(0, 3, '薪资')
    for i in range(nums):
        sheet_1.write(i+1,0,read_json(html,i)[0])
        sheet_1.write(i+1,1,read_json(html,i)[1])
        sheet_1.write(i+1,2,read_json(html,i)[2])
        sheet_1.write(i+1,3,read_json(html,i)[3])
    new_excel.save('智联招聘.xls')
html=request_zhilian()
time.sleep(3)
create_excel()
time.sleep(1)
addTo_excel(html,9)

