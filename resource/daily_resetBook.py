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

print("即将开始每日【WhereMyLife】的签到...")
time.sleep(3)
print("正在加载签到模块...")
time.sleep(3)
print("请求签到中...")
url='http://wheremylife.cn/1.0/user/resetBook'
cookies={'wml:key':'eyJldmVudHMiOltdLCJjYXB0Y2hhVG9rZW4iOiJicHBhaCIsInVzZXJpZCI6MzU2NDUsIl9leHBpcmUiOjE2NTc1MjI4MDEwNzIsIl9tYXhBZ2UiOjYwNDgwMDAwMH0'}
headers={'User-Agent':'Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/103.0.5060.114Safari/537.36Edg/103.0.1264.49','Accept':'*/*','Accept-Encoding':'gzip,deflate','Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6','Cache-Control':'no-cache','Content-Length':'2','Content-Type':'application/json','Cookie':'wml:key=eyJldmVudHMiOltdLCJjYXB0Y2hhVG9rZW4iOiJicHBhaCIsInVzZXJpZCI6MzU2NDUsIl9leHBpcmUiOjE2NTc1MjI4MDEwNzIsIl9tYXhBZ2UiOjYwNDgwMDAwMH0=;wml:key.sig=YmAEjWDiQGyvg1izUxJR7p1RFFY','DNT':'1','Host':'wheremylife.cn','Origin':'http://wheremylife.cn','Pragma':'no-cache','Proxy-Connection':'keep-alive','Referer':'http://wheremylife.cn/home'}
a={"username": "3031147044@qq.com", "password": "MuSTAR1234"}
x=requests.post(url, headers=headers, json=a,timeout=2.50)
time.sleep(10)
check_in_result=str(x.text)
message="success" in  check_in_result
if message==True:
    result="打卡成功！"
else:
    result="打卡失败，原因是 " + x.text 
print(result)


time.sleep(1)
print("正在调用钉钉返回登陆结果")
timestamp = str(round(time.time() * 1000))
secret ="SECe65b044d5043cd96f209aafdfd709c2238d58da3a12437ffa612338aee672f27"
secret_enc = secret.encode('utf-8')
string_to_sign = '{}\n{}'.format(timestamp, secret)
string_to_sign_enc = string_to_sign.encode('utf-8')
hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
timestamp=int(timestamp)
#https://oapi.dingtalk.com/robot/send?access_token=03ac7e7e59a3e607c024ce3dc023ceb748169a949ec747cbf6d689976facd625&timestamp=XXX&sign=XXX
web="https://oapi.dingtalk.com/robot/send?access_token=03ac7e7e59a3e607c024ce3dc023ceb748169a949ec747cbf6d689976facd625&timestamp=%a&sign="%(timestamp)
link=web+sign



import requests,json   #导入依赖库
headers={'Content-Type': 'application/json'}   #定义数据类型
#定义要发送的数据
#"at": {"atMobiles": "['"+ mobile + "']"
data = {
    "msgtype": "text",
    "text": {"content": result},
    "isAtAll": True}
res = requests.post(link, data=json.dumps(data), headers=headers)   #发送post请求

print(res.text)
print("全部任务已完成")
time.sleep(3)
