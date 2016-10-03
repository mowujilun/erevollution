import pymysql
coon = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='erevollution', charset='UTF8')
cur = coon.cursor()
cur.execute("select * from baseinfo")
for i in cur:
    print(i)
cur.close()
coon.close()