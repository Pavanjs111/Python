import mysql.connector as mc
con_obj = mc.connect(user="root", password="root",host="localhost", database="j4ym7")
print(con_obj)
cur_obj=con_obj.cursor()

try:
    cur_obj.execute("create table students (id int(10), name varchar(20), branch varchar(20),phone int(10), address varchar(20), marks int(3))")
    print("table created")

    
except:
    print("connection not established")

con_obj.close()