import mysql.connector

# Connexion à la base de données
connexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Klarette69$",
    database="LaPlateforme"
)

curseur_1 = connexion.cursor(buffered=True)
curseur_2 = connexion.cursor(buffered=True)

requete_1 = "SELECT * FROM employes WHERE salaire > 3000;"
requete_2 = "SELECT * FROM employes INNER JOIN services ON employes.id_service = services.id;"

curseur_1.execute(requete_1)
curseur_2.execute(requete_2)

resultat_1 = curseur_1.fetchall()
resultat_2 = curseur_2.fetchall()

print(f"Les employés ayant un salaire supérieur à 3000 euros : \n{resultat_1}")
print(f"Les employés et leur service respectif : \n{resultat_2}")

curseur_1.close()
curseur_2.close()
