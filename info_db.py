import pymysql

def infodb():
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='000000', db='bilibili', charset='utf8')
    cursor = conn.cursor()
    sql='create table bili_info ( id int unsigned auto_increment primary key not null,birthday varchar(20),mid varchar(10),face varchar(150),current_level varchar(30),name varchar(20),desca varchar(80),sex varchar(10),signa varchar(30),vipType varchar(5),vipStatus varchar(5),following varchar(10),follower varchar(10),archive varchar(10),article varchar(10));'
    cursor.execute(sql)
    conn.commit()
infodb()