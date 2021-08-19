import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "cadastro"
)

mycursor = mydb.cursor()

mycursor.execute("Select * from gafanhotos")
mycursor.execute("Select * from gafanhotos")
mycursor.execute("Select * from gafanhotos")
mycursor.execute("Select * from gafanhotos")
mycursor.execute("Select * from gafanhotos")
mycursor.execute("Select * from gafanhotos")
mycursor.execute("Select * from gafanhotos")
mycursor.execute("Select * from gafanhotos")
mycursor.execute("Select * from gafanhotos")
mycursor.execute("Select * from gafanhotos")
mycursor.execute("Select * from gafanhotos")
mycursor.execute("Select * from gafanhotos")
mycursor.execute("Select * from gafanhotos")
mycursor.execute("Select * from gafanhotos")
mycursor.execute("Select * from gafanhotos")
mycursor.execute("Select * from gafanhotos")
mycursor.execute("Select * from gafanhotos")
mycursor.execute("Select * from gafanhotos")

myresult = mycursor.fetchall()

for x in myresult:
    print('cod'  x[0], x[1])