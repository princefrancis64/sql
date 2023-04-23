import mysql.connector as conn

mydb = conn.connect(host = "localhost" , user = 'root', passwd = "Letsgo1247")
cursor = mydb.cursor()
#cursor.execute("insert into prince.ineuron values(101, 'Prince Francis','prince.francis64',1000,30)")
#mydb.commit()
cursor.execute("select * from prince.ineuron")
for i in cursor.fetchall():
    print(i)