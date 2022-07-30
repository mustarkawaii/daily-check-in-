from operator import truediv
from tkinter import N
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
WhereMyLife_headers={'User-Agent':'Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/103.0.5060.114Safari/537.36Edg/103.0.1264.49','Accept':'*/*','Accept-Encoding':'gzip,deflate','Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6','Cache-Control':'no-cache','Content-Length':'2','Content-Type':'application/json','Cookie':'wml:key=eyJldmVudHMiOltdLCJ1c2VyaWQiOjM1NjQ1LCJfZXhwaXJlIjoxNjU5NTcxNDY3MTQ2LCJfbWF4QWdlIjo2MDQ4MDAwMDB9; wml:key.sig=Rdob-uKaDQZLwjortevV0ZEp_2M','DNT':'1','Host':'wheremylife.cn','Origin':'http://wheremylife.cn','Pragma':'no-cache','Proxy-Connection':'keep-alive','Referer':'http://wheremylife.cn/home'}
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
print("请求签到中...")
gtloli_url='https://www.gtloli.gay/plugin.php?id=k_misign:sign&operation=qiandao&format=button&formhash=70884e41&inajax=1&ajaxtarget=midaben_sign'
gtloli_headers={'accept':'*/*','accept-encoding':'gzip, deflate, br','accept-language':'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6','cookie':'uLXw_2132_saltkey=B1E1F311; uLXw_2132_lastvisit=1658226030; uLXw_2132_auth=1455gVbwu5DLrCimcUzTWOFNQwD22OU3676SCN84n7GhnC%2Bs9upUbYX6BdmmmSXffihQCh2vx36yMUuDxfwiYMfsqbM; uLXw_2132_lastcheckfeed=965230%7C1658483292; uLXw_2132_nofavfid=1; uLXw_2132_atarget=1; uLXw_2132_taskdoing_965230=1; uLXw_2132_forum_lastvisit=D_2_1658541522D_90_1658541789D_191_1658542320; uLXw_2132_smile=2D1; uLXw_2132_visitedfid=191D141D84D90D97D2D88; uLXw_2132_sid=0; uLXw_2132_onlineusernum=1188; uLXw_2132_ulastactivity=1658650137%7C0; uLXw_2132_sendmail=1; uLXw_2132_lastact=1658650138%09home.php%09spacecp; uLXw_2132_noticeTitle=1','dnt':'1','referer':'https ://www.gtloli.gay/forum.php','sec-ch-ua':'" Not;A Brand";v="99", "Microsoft Edge";v="103", "Chromium";v="103"','sec-ch-ua-mobile':'?0','sec-ch-ua-platform':'"Windows"','sec-fetch-dest':'empty','sec-fetch-mode':'cors','sec-fetch-site':'same-origin','user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.62','x-requested-with':'XMLHttpRequest'}
requests.DEFAULT_RETRIES = 5
s = requests.session()
s.keep_alive = False
y=requests.get(url=gtloli_url, headers=gtloli_headers, timeout=5)
time.sleep(5)
gtloli_check_in_result=y.status_code

if gtloli_check_in_result==200:
    gtloli_result="gtloli签到成功！"
else:
    gtloli_result="gtloli莫名奇妙签到失败了 " + "HTTP错误代号【"  + gtloli_check_in_result + "】"
time.sleep(5)
print(gtloli_result)








all_result="综上所述:"  + "1." + WhereMyLife_result  +"2." + gtloli_result + "以上."
print(all_result)
