# -*- coding:utf-8 -*-
'''
Created on 2017年10月18日

@author: jeff.yang
'''
from urllib.request import Request, urlopen
from lxml import etree

url = "http://www.xinhuanet.com/politics/19cpcnc/zb/gov1/wzsl.htm"
request = Request(url)
response = urlopen(request)
content = response.read()
html = etree.HTML(content)
msgList = html.xpath('//div[@class="wzsl"]/div')

with open('test.txt', 'w', encoding='gbk') as f:
    i = 1
    while i <= len(msgList):
        message = html.xpath('//div[@class="wzsl"]/div[' + str(i) + ']/div/p/text()')
        print(message[0])
        f.write(message[0]+'\n')
        i = i + 1
print('Done!')