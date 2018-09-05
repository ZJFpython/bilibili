import pymysql
import pandas as pd
def write(file):
    dict1={
        'host': '127.0.0.1',
        'port': 3306,
        'user': 'root',
        'passwd': '000000',
        'db': 'bilibili',
        'charset': 'utf8'
    }
    cn=pymysql.connect(**dict1)
    hand=cn.cursor()
    A=open(file,'r')
    a=pd.read_csv(A)

    for i in range(a.shape[0]):
        # print(i)
        birthday=a.iloc[i,0]
        mid=a.iloc[i,1]
        face=a.iloc[i,2]
        current_level=a.iloc[i,3]
        name=a.iloc[i,4]
        desca=a.iloc[i,5]
        sex=a.iloc[i,6]
        signa=a.iloc[i,7]
        vipType=a.iloc[i,8]
        vipStatus=a.iloc[i,9]
        following=a.iloc[i,10]
        follower=a.iloc[i,11]
        archive=a.iloc[i,12]
        article=a.iloc[i,13]

        hand.execute("insert into bili_info values(0,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(str(birthday),str(mid),str(face),str(current_level),str(name),str(desca),str(sex),str(signa),str(vipType),str(vipStatus),str(following),str(follower),str(archive),str(article)))
        cn.commit()
if __name__ == '__main__':
    write(file='输入文件名')
