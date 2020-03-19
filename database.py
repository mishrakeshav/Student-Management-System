import mysql.connector  
from mysql.connector import errorcode

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "root",
    database = "SMS"
)
my_cursor = mydb.cursor()
# if mydb :
#     cursor = mydb.cursor()
#     cursor.execute("UPDATE students SET name = 'MISHRA' WHERE rollno = 31")
#     cursor.execute("SELECT * FROM students")
#     for data in cursor:
#         print(data)
#     # rollbacks to the previous state
#     mydb.rollback() 
# try:
#     eid = 12
#     ename = "Jaideep More"
#     marks = 100
#     sql = "INSERT INTO students VALUES(%d, '%s', %d)"
#     data = (int(eid), ename, int(marks))
#     my_cursor.execute(sql%data) 
#     mydb.commit()
    
# except mysql.connector.errors.IntegrityError:
#     print("already exists")

try:
    eid = 12
    ename = "Jaideep More"
    marks = 100
    sql = "SELECT * FROM students WHERE rollno = %d"
    data = (int(eid))
    my_cursor.execute(sql%data)
    val = None 
    print(my_cursor.fetchall())
    
    if val :
        print(val)
    else:
        print("Does not exist")
    # mydb.commit()
    
except mysql.connector.errors.IntegrityError:
    print("already exists")