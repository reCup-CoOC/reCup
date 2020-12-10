#Emprunt d'un nombre de tasse défini en paramètre

import mysql.connector

conn = mysql.connector.connect(host="localhost",
                               user="phpmyadmin", password="Vince@Mysql1997",
                               database="reCup")
cursor = conn.cursor()


#IDENTIFICATION PAR BADGE DE L'UTILISATEUR

id_user = input("Entrez votre identifiant d'utilisateur : ")

#REQUETE DE RECUPERATION DES INFORMATIONS DE L'UTILISATEUR QUI A BADGE
query  = ("SELECT * FROM Utilisateur WHERE ID_USERS=%s ")

cursor.execute(query, (id_user, ))
rows = cursor.fetchall()
for row in rows:
   #print('{0} : {1} - {2}'.format(row[0], row[1], row[2]))
   nb_tasses_empruntees = row[5] #Recuperation du nombre de tasses
   solde = row[6]  #Recuperation du solde


new_nb_tasses_empruntees = nb_tasses_empruntees - 1 #Calcul du nombre total de tasses empruntees
caution = 2 #Caution de 2€ rendue suite au depot

#MODIFICATION DU NOMBRE DE TASSES EMPRUNTEES ET DU SOLDE DE L'UTILISATEUR
solde = solde + caution
solde = str(solde)
new_nb_tasses_empruntees = str(new_nb_tasses_empruntees)
sql = "UPDATE Utilisateur SET nb_tasses_empruntees = %s, solde=%s WHERE ID_USERS =%s"

cursor.execute(sql, (new_nb_tasses_empruntees, solde, id_user)) #Cree une requete pour decrementer le nombre total de tasses empruntees  

conn.commit() #Envoie la requête à la base de données

conn.close()

