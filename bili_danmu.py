import requests
import re
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')
url='http://api.bilibili.com/x/v1/dm/list.so?oid=50083046'
headers={

'Host': 'api.bilibili.com',
'Connection': 'keep-alive',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/6.2.4094.1 Safari/537.36',
'Origin': 'https://www.bilibili.com',
'Accept': '*/*',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'zh-CN,zh;q=0.8',
'If-Modified-Since': 'Sat, 11 Aug 2018 23:25:43 GMT'


}
mm=open('弹幕.xml','wb')
res=requests.get(url=url,headers=headers,verify=False).content
mm.write(res)
print(res)
danmu1 =re.findall(b'">(.*?)</d>',res)
with open('弹幕.txt','wb') as f:
    for danmu in danmu1:
        danmu=danmu.decode('utf-8').encode('utf-8')
        x='\n'
        x=x.encode('utf-8')
        f.write(danmu)
        f.write(x)