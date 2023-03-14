import mysql.connector 

lb = mysql.connector.connect(
    host = "localhost",
    user ="root",
    password = "Klarette69$",
    database = "Laplateforme"
)

cursor = lb.cursor()

cursor.execute("SELECT SUM(capacite) FROM salles")

resultat = cursor.fetchone()

print("La capacité de toutes les salles est de :", resultat[0])

cursor.close()
lb.close()




