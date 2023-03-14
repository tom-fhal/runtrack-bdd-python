import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Klarette69$",
  database="LaPlateforme"
)

lb = mydb.cursor()

lb.execute("SELECT nom, capacite FROM salles")

resultats = lb.fetchall()

print(resultats)
lb.close()
mydb.close()
