import requests
list1=[]
p='114.113.126.87:80'
url='https://www.baidu.com'
res=requests.get(url,proxies={'https':p})
print(res.status_code)
list1.append(p)
