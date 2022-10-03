import mysql.connector as mc
con_obj = mc.connect(user="root", password="root",host="localhost")
print(con_obj)
cur_obj=con_obj.cursor()
try:
    cur_obj.execute("select * from j4ym7.students where id=123 ")
except:
    con_obj.rollback()

for db in cur_obj:
    print(db)

con_obj.close()