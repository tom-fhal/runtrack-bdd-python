import mysql.connector 

lb = mysql.connector.connect(
    host = "localhost",
    user ="root",
    password = "Klarette69$",
    database = "Laplateforme"
)

cursor = lb.cursor()

cursor.execute("SELECT SUM(superficie) FROM etage")

resultat = cursor.fetchone()

print("La superficie de La Plateforme est de", resultat[0], "m2")

cursor.close()
lb.close()




