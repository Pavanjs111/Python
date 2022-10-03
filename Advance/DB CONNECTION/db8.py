import mysql.connector as mc
con_obj = mc.connect(user="root", password="root",host="localhost")
print(con_obj)
cur_obj=con_obj.cursor()
try:
    # cur_obj.execute("delete from j4ym7.students where id=123")
    # cur_obj.commit()
    cur_obj.execute("select * from j4ym7.students")

except:
    con_obj.rollback()

for db in cur_obj:
    print(db)
# print(cur_obj.rowcount,"rows are deleted")
con_obj.close()