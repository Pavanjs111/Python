import mysql.connector as mc
con_obj = mc.connect(user="root", password="root",host="localhost", database="j4ym7")
print(con_obj)
cur_obj=con_obj.cursor()
try:
    cur_obj.execute("insert into j4ym7.students(id,name,branch,phone,address,marks) values(123,'chadanand','mech','12451479','hosdurga',85)")
    con_obj.commit()
    print("commited")
except:
    con_obj.rollback()

con_obj.close()