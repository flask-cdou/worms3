import requests
import random
import json
import time
import datetime
import hashlib
import navigator
url= 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
# strhtml=requests.get(url)
# print(strhtml.text)
#生成系统时间
def date_time_milliseconds(date_time_obj):
    return int(time.mktime(date_time_obj.timetuple()) * 1000)


key=input("输入要查询的词句：")
lts=date_time_milliseconds(datetime.datetime.utcnow())
salt=date_time_milliseconds(datetime.datetime.utcnow())+random.randint(1,10)
# sign=hashlib.md5(('fanyideskweb' + key + str(salt) + 'Nw(nmmbP%A-r6U3EUn]Aj').encode('utf-8'))
sign=hashlib.md5(("fanyideskweb" + key + str(salt) + "Tbh5E8=q6U3EXe+&L[4c@").encode('utf-8')).hexdigest()
bv=hashlib.md5(("5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36".encode('utf-8'))).hexdigest()
headers = {
    "Cookie": "OUTFOX_SEARCH_USER_ID=1721894360@59.111.179.141; _ntes_nnid=28c86721ce2c2392d0b4bc1c066195c2,1562810189644; OUTFOX_SEARCH_USER_ID_NCOO=1717529083.05212; P_INFO=qducst_xmt@163.com|1572920094|0|other|00&99|shd&1572744638&mail163#shd&null#10#0#0|&0|mail163|qducst_xmt@163.com; JSESSIONID=aaadMecWfzOYVgeMhs8dx; ___rl__test__cookies=1584780646068",
    "Referer": "http://fanyi.youdao.com/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
}

formdata={
  "i": key,
  "from": "AUTO",
  "to": "AUTO",
  "smartresult": "dict",
  "client": "fanyideskweb",
  "salt": salt,
  "sign": sign,
  "lts": lts,
  "bv": bv,
  "doctype": "json",
  "version": "2.1",
  "keyfrom": "fanyi.web",
  "action": "FY_BY_REALTlME"
}
response = requests.post(url,data=formdata,headers=headers)
content = json.loads(response.text)
result_content=content['translateResult'][0][0]['tgt']
print("%s翻译结果：%s"%(key,result_content))
