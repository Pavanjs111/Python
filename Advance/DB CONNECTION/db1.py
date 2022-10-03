import mysql.connector as mc
con_obj = mc.connect(user="root", password="root",host="localhost")
print(con_obj)