import mysql.connector as mc
con_obj = mc.connect(user='root', password='root',host='localhost')
cur_obj=con_obj.cursor()

try:
    cur_obj.execute("create database j4ym7") 
    print("database created")
except:
    print("connection not established")


con_obj.close()
