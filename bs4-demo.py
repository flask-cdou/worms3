from bs4 import BeautifulSoup
import requests
import re

url='http://www.cntour.cn/'
strhtml=requests.get(url)

soup= BeautifulSoup(strhtml.text,'lxml')
data= soup.select('#main > div > div.mtop.firstMod.clearfix > div.centerBox > ul.newsList > li > a')
print(data)
# 2.5 清洗和组织数据
for item in data:
    results={
        'title': item.get_text(),
        'link': item.get('href'),
        'id'  : re.findall('\d+',item.get('href'))
    }
    print(results)