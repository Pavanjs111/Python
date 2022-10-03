import mysql.connector as mc
con_obj = mc.connect(user='root', password='root',host='localhost')
cur_obj=con_obj.cursor()

try:
    cur_obj.execute('show databases')
    for db in cur_obj:
        print(db)
    
except:
    print("connection object not eatablished")


con_obj.close()