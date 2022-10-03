import mysql.connector as mc
con_obj = mc.connect(user="root", password="root",host="localhost")
print(con_obj)
cur_obj=con_obj.cursor()

try:
    qry="insert into j4ym7.students(id,name,branch,phone,address,marks) values(%s,%s,%s,%s,%s,%s)"
    val=[
        (123,'Pavan','CSE','1245698','Banglore',100),
        (124,'Meenal','CSE','12451484','Gulbarga',80),
        (125,'Krishna','BCA','1245845','Bellary',95),
        (126,'Mythri','CSE','12458796','Sirsi',90),
        (127,'Keerthana','MSc','1248795','Jayanagar',82),
        (128,'Kavyashree','CSE','7451789','Hell',90),
        (129,'Jish','BCA','1578469','BAnglore',78),
    ]
    cur_obj.executemany(qry,val)
    con_obj.commit()
    print("the quiries are inserted")

except:
    con_obj.rollback()


print(cur_obj.rowcount, "rows are inserted")
con_obj.close()