from operator import truediv
import requests
import json
import time
import time
import hmac
import hashlib
import base64
import urllib.parse
import json
import requests
import sys

print("开始准备签到WhereMyLife....")
time.sleep(3)
print("即将开始每日【WhereMyLife】的签到...")
time.sleep(3)
print("正在加载签到模块...")
time.sleep(3)
print("请求签到中...")
WhereMyLife_url='http://wheremylife.cn/1.0/user/resetBook'
WhereMyLife_headers={'User-Agent':'Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/103.0.5060.114Safari/537.36Edg/103.0.1264.49','Accept':'*/*','Accept-Encoding':'gzip,deflate','Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6','Cache-Control':'no-cache','Content-Length':'2','Content-Type':'application/json','Cookie':'wml:key=eyJldmVudHMiOltdLCJ1c2VyaWQiOjM1NjQ1LCJfZXhwaXJlIjoxNjU4OTA5NDcxNDYyLCJfbWF4QWdlIjo2MDQ4MDAwMDB9; wml:key.sig=OKaY20e-GBLR4XmkiWkuFuJtoyE','DNT':'1','Host':'wheremylife.cn','Origin':'http://wheremylife.cn','Pragma':'no-cache','Proxy-Connection':'keep-alive','Referer':'http://wheremylife.cn/home'}
WhereMyLife_json={"username": "3031147044@qq.com", "password": "MuSTAR1234"}
x=requests.post(url=WhereMyLife_url, headers=WhereMyLife_headers, json=WhereMyLife_json,timeout=2.50)
time.sleep(5)
WhereMyLife_check_in_result=str(x.text)
WhereMyLife_message="success" in  WhereMyLife_check_in_result

WhereMyLife_day_url='http://wheremylife.cn/1.0/user/book'
day=requests.get(url=WhereMyLife_day_url, headers=WhereMyLife_headers, json=WhereMyLife_json,timeout=2.50)
WhereMyLife_day=str(day.text)
WhereMyLife_day=WhereMyLife_day[9:11]

if WhereMyLife_message==True:
   WhereMyLife_result="WhereMyLife打卡成功！剩余重置天数为" + str(14) + "天"
else:
    WhereMyLife_result="WhereMyLife打卡失败，原因是【" + x.text  + "】，剩余重置天数为" + WhereMyLife_day +"天"    
print(WhereMyLife_result)

time.sleep(1)
print("开始准备签到gtloli...")
time.sleep(3)
print("即将开始每日【gtloli】的签到...")
time.sleep(3)
print("暂未开放！")
time.sleep(3)
