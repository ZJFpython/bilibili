import requests
import re
from lxml import etree
import json
import os
from multiprocessing import Pool
import time
def sub(s):
    patn_1 = re.compile(r'\?')
    patn_2 = re.compile(r'\/')
    patn_3 = re.compile(r'\\')
    patn_4 = re.compile(r'\|')
    patn_5 = re.compile(r'\:')
    patn_6 = re.compile(r'\<')
    patn_7 = re.compile(r'\>')
    patn_8 = re.compile(r'\*')
    patn_9 = re.compile(r'\:')

    s = re.sub(patn_1, "", s)
    s = re.sub(patn_2, "", s)
    s = re.sub(patn_3, "", s)
    s = re.sub(patn_4, "", s)
    s = re.sub(patn_5, "", s)
    s = re.sub(patn_6, "", s)
    s = re.sub(patn_7, "", s)
    s = re.sub(patn_8, "", s)
    s = re.sub(patn_9, "", s)
    return s


def run(url_av):
    av=re.findall(r'av(\d+)',url_av)[0]
    av=int(av)
    p=re.findall(r'p=(\d+)',url_av)[0]
    p=int(p)
    headers1={

            'Host': 'www.bilibili.com',
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/6.2.4094.1 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Referer': 'https://space.bilibili.com/'+str(av)+'/',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Cookie': 'LIVE_BUVID=AUTO5815176538131040; buvid3=AE73922F-01DD-4DE6-B8E5-7FC04578DAC831024infoc; rpdid=xwsowqqwwdosommsikiw; fts=1517752500; pgv_pvi=9525556224; sid=ln5r884w; CNZZDATA2724999=cnzz_eid%3D126824076-1517748234-https%253A%252F%252Fwww.bilibili.com%252F%26ntime%3D1521439898; finger=7360d3c2; UM_distinctid=1651d719bfa1-0f309769228c1f-4a531929-1fa400-1651d719bfc1b5; DedeUserID=25544000; DedeUserID__ckMd5=dd49b9bb77ff1b0b; SESSDATA=a5e43f29%2C1536575045%2Ce0f48515; bili_jct=bb6fcbe60ce12800e8af173669ce5d5b; CURRENT_FNVAL=8; stardustvideo=0; CURRENT_QUALITY=80; _dfcaptcha=b9760efe6f882dc0ecd732431b9bc0f0'
        }

    res1=requests.get(url=url_av,headers=headers1).text
    url_patn = re.findall(r'"url":"(.*?)","backup_url"', res1)


    #获取标题
    url_biaoti='https://api.bilibili.com/x/player/pagelist?aid='+str(av)+'&jsonp=jsonp'

    headers2={

            'Host': 'api.bilibili.com',
    'Connection': 'keep-alive',
    'Accept': '*/*',
    'Origin': 'https://www.bilibili.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/6.2.4094.1 Safari/537.36',
    'Referer': 'https://www.bilibili.com/video/av'+str(av)+'/?p='+str(p),
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Cookie': 'LIVE_BUVID=AUTO5815176538131040; buvid3=AE73922F-01DD-4DE6-B8E5-7FC04578DAC831024infoc; rpdid=xwsowqqwwdosommsikiw; fts=1517752500; pgv_pvi=9525556224; sid=ln5r884w; finger=7360d3c2; UM_distinctid=1651d719bfa1-0f309769228c1f-4a531929-1fa400-1651d719bfc1b5; DedeUserID=25544000; DedeUserID__ckMd5=dd49b9bb77ff1b0b; SESSDATA=a5e43f29%2C1536575045%2Ce0f48515; bili_jct=bb6fcbe60ce12800e8af173669ce5d5b; CURRENT_FNVAL=8; stardustvideo=0; CURRENT_QUALITY=80; _dfcaptcha=cfa5c8f7d1163a027db3348f5884da1d'
        }
    res2=requests.get(url=url_biaoti,headers=headers2).text
    res2=json.loads(res2)
    title=res2['data'][p-1]['part']
    k=0
    for j in url_patn:
        k+=1
        host_patn = re.findall('http://(.*?)/upgcxcode', j)
        # print(j)
        # print(host_patn[0])
        headers3 = {
                'Host': host_patn[0],
                'Connection': 'keep-alive',
                'Origin': 'https://www.bilibili.com',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
                'Accept': '*/*',
                'Referer': 'https://www.bilibili.com/video/av'+str(av)+'/',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'zh-CN,zh;q=0.9',
            }
        biaoti=sub(title+str(k))
        path = r"E:/video/"+title+"/"
        if not os.path.isdir(path):
            os.makedirs(path)
            if not os.path.exists(path+biaoti+'.mp4'):
                with open(path+biaoti+'.mp4','ab') as ff:
                    print(biaoti,'正在下载中')
                    ff.write(requests.get(url=j, headers=headers3).content)
                    print(biaoti, '下载完成')
            else:
                print('此视频已存在')
        else:
            if not os.path.exists(path + biaoti + '.mp4'):
                with open(path+biaoti+'.mp4','ab') as ff:
                    print(biaoti,'正在下载中')
                    ff.write(requests.get(url=j, headers=headers3).content)
                    print(biaoti, '下载完成')
            else:
                print('此视频已存在')

def start(p,url_base):
    pool=Pool(1)
    list_url=[]
    for gg in range(1,p+1):
        url=url_base+str(gg)
        list_url.append(url)
    pool.map(run,list_url)
    pool.close()
    pool.join()

if __name__ == '__main__':
    start(1,'https://www.bilibili.com/video/av15112353/?p=')

