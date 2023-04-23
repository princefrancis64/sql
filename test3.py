import mysql.connector as conn
mydb = conn.connect(host = "localhost",user = "root" , passwd = "Letsgo1247")
cursor = mydb.cursor()
cursor.execute("select employee_id,emp_mailid from prince.ineuron")
l=[]
for i in cursor.fetchall():
    l.append(i)

print(l)
