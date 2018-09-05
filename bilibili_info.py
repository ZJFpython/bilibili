import re
import requests
import json
import csv
from multiprocessing import Pool
import random
def run(i):

    url='https://space.bilibili.com/ajax/member/GetInfo'

    headers1={
    'Accept':'application/json, text/plain, */*',
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'zh-CN,zh;q=0.8',
    'Connection':'keep-alive',
    'Content-Length':'49',
    'Content-Type':'application/x-www-form-urlencoded',
    'Cookie':'finger=7360d3c2; LIVE_BUVID=AUTO7815343364860617; sid=km4howqt; DedeUserID=25544000; DedeUserID__ckMd5=dd49b9bb77ff1b0b; SESSDATA=a5e43f29%2C1536928530%2Cd7611cfe; bili_jct=1c69e0b8fe29b4af0b07a331d0a1cd46; buvid3=0EABD44A-6D96-4C86-AAC7-5D9707438BE06691infoc; bsource=seo_baidu; _dfcaptcha=41c63d5edb4e65377b1a26edadca0da8; fts=1534336536; UM_distinctid=1653d9591cd5db-0f7fcf8780c432-b373f68-144000-1653d9591ce34b; CNZZDATA2724999=cnzz_eid%3D688060569-1534335219-https%253A%252F%252Fwww.bilibili.com%252F%26ntime%3D1534335219',
    'Host':'space.bilibili.com',
    'Origin':'https://space.bilibili.com',
    'Referer':'https://space.bilibili.com/'+str(i)+'/',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36'
    }
    data={
        'mid':str(i),
    'csrf':'1c69e0b8fe29b4af0b07a331d0a1cd46'
    }
    res=requests.post(url=url,data=data,headers=headers1).json()
    status=res['status']
    # print(status)

    if status==True:
        url1='https://api.bilibili.com/x/relation/stat?vmid='+str(i)+'&jsonp=jsonp&callback=__jp4'
        headers2={
            'Accept':'*/*',
        'Accept-Encoding':'gzip, deflate, sdch, br',
        'Accept-Language':'zh-CN,zh;q=0.8',
        'Connection':'keep-alive',
        'Cookie':'finger=7360d3c2; LIVE_BUVID=AUTO7815343364860617; sid=km4howqt; DedeUserID=25544000; DedeUserID__ckMd5=dd49b9bb77ff1b0b; SESSDATA=a5e43f29%2C1536928530%2Cd7611cfe; bili_jct=1c69e0b8fe29b4af0b07a331d0a1cd46; buvid3=0EABD44A-6D96-4C86-AAC7-5D9707438BE06691infoc; fts=1534336536; UM_distinctid=1653d9591cd5db-0f7fcf8780c432-b373f68-144000-1653d9591ce34b; rpdid=kwqwspoxqldoskpkkqspw; CURRENT_FNVAL=2; stardustvideo=1; _dfcaptcha=41c63d5edb4e65377b1a26edadca0da8',
        'Host':'api.bilibili.com',
        'Referer':'https://space.bilibili.com/'+str(i)+'/',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36'

        }

        data1={
            'vmid':str(i),
        'jsonp':'jsonp',
        'callback':'__jp4'
        }
        res1=requests.get(url=url1,params=data1,headers=headers2).text
        res1 = res1.replace('__jp4(', '', 1)
        res1 = res1.replace(')', '', 1)
        res4 = json.loads(res1)
        following = res4['data']['following']
        follower = res4['data']['follower']

        if follower>100:
            ff=open('messages7.csv','a')
            try:
                birthday=res['data']['birthday']
            except:
                birthday='无信息'

            try:
                face=res['data']['face']
            except:
                face='无信息'
            try:
                mid=res['data']['mid']
            except:
                mid='无信息'
            try:
                current_level=res['data']['level_info']['current_level']
            except:
                current_level='无信息'
            try:
                name=res['data']['name']
            except:
                name='无信息'
            try:
                desc=res['data']['official_verify']['desc']
            except:
                desc='无信息'
            try:
                sex=res['data']['sex']
            except:
                sex='无信息'
            try:
                sign=res['data']['sign']
            except:
                sign='无信息'
            try:
                vipType=res['data']['vip']['vipType']
            except:
                vipType='无信息'
            try:
                vipStatus=res['data']['vip']['vipStatus']
            except:
                vipStatus='无信息'


            url2='https://api.bilibili.com/x/space/upstat?mid='+str(i)+'&jsonp=jsonp&callback=__jp5'
            headers3={
                'Accept':'*/*',
            'Accept-Encoding':'gzip, deflate, sdch, br',
            'Accept-Language':'zh-CN,zh;q=0.8',
            'Connection':'keep-alive',
            'Cookie':'finger=7360d3c2; LIVE_BUVID=AUTO7815343364860617; sid=km4howqt; DedeUserID=25544000; DedeUserID__ckMd5=dd49b9bb77ff1b0b; SESSDATA=a5e43f29%2C1536928530%2Cd7611cfe; bili_jct=1c69e0b8fe29b4af0b07a331d0a1cd46; buvid3=0EABD44A-6D96-4C86-AAC7-5D9707438BE06691infoc; fts=1534336536; UM_distinctid=1653d9591cd5db-0f7fcf8780c432-b373f68-144000-1653d9591ce34b; rpdid=kwqwspoxqldoskpkkqspw; CURRENT_FNVAL=2; stardustvideo=1; _dfcaptcha=41c63d5edb4e65377b1a26edadca0da8',
            'Host':'api.bilibili.com',
            'Referer':'https://space.bilibili.com/'+str(i)+'/',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36'

            }

            data2={
                'vmid':str(i),
            'jsonp':'jsonp',
            'callback':'__jp5'
            }

            res2=requests.get(url=url2,params=data2,headers=headers3).text
            res2 = res2.replace('__jp5(', '', 1)
            res2 = res2.replace(')', '', 1)
            res3 = json.loads(res2)
            archive=res3['data']['archive']['view']
            article = res3['data']['article']['view']
            try:

                list1 = [birthday,mid,face,current_level,name,desc,sex,sign,vipType,vipStatus,following,follower,archive,article]
                csv_w = csv.writer(ff)
                csv_w.writerow(list1)
                print(list1)
                print('第%s位用户的信息写入完成' % i)
            except:
                print('第%s位用户无信息'%i)
    else:
        print('无信息aaa')

def start(item=None,start_page=1,end_page=1000,num=100):
    pool=Pool(item)
    page=random.sample(range(start_page,end_page),num)
    pool.map(run,page)
    pool.join()
    pool.close()

if __name__ == '__main__':
    start(item=2,start_page=1000,end_page=2000)

