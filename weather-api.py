# -*- encoding: utf-8 -*-
import requests
import pandas as pd
import time
import json

url='https://cdn.heweather.com/china-city-list.txt'
strhtml= requests.get(url)
strhtml.encoding= 'utf-8' #把requests对象进行编码转换，否则乱码。
data= strhtml.text
data=data.replace(' ','') #去掉data数据中的空格，否则再使用pandas获取城市ID时找不到列名
#把数据以文本形式存到代码目录
with open('./data.txt','w',encoding='utf-8') as f:
    f.write(data)
#读取data.txt数据作为dataframe对象，以便后续遍历城市ID↓
df=pd.read_csv('./data.txt',header=3,sep='|').dropna(axis=1) #dorpna 1是按行删除空值列
# print(df['城市ID'])
for id in df['城市ID'][1:]:
    print("id:",id)
    #根据网站提供的API接口文档写访问的URL 第一个：3天预测；第二个：今天天气;第三个：城市信息
    url_3d ="https://devapi.qweather.com/v7/weather/3d?location="+id+"&key=d910b0c0ca62429a9e9e278ae3f3276c"
    url_weather = "https://devapi.qweather.com/v7/weather/now?location="+id+"&key=d910b0c0ca62429a9e9e278ae3f3276c"
    url_city = "https://geoapi.qweather.com/v2/city/lookup?location="+id+"&key=d910b0c0ca62429a9e9e278ae3f3276c"
    print(url_3d)
    weather_results=requests.get(url_3d)
    time.sleep(2) #每2秒读取一次数据
    # print(weather_results.text)#打印读取内容
    dic= weather_results.json()
    #打印3天里的第一天预报
    print(str(dic['daily'][0]).replace(' ',''))