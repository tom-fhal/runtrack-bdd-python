import mysql.connector 

lb = mysql.connector.connect(
    host = "localhost",
    user ="root",
    password = "Klarette69$",
    database = "Laplateforme"
)

cursor = lb.cursor()

cursor.execute("SELECT nom, capacite FROM salles")

resultat = cursor.fetchall()

tuples = []
for x in resultat:
   tuples.append((x[0], x[1]))

print(tuples)