#Emprunt d'un nombre de tasse défini en paramètre

import mysql.connector




def identification_sql(badge_id):


    conn = mysql.connector.connect(host="localhost",
                                   user="superuser", password="bonjour",
                                   database="Recup")
    cursor = conn.cursor()
    id_user = badge_id[1:-1] #A REMPLACER PAR LA BADGEUSE

    #REQUETE DE RECUPERATION DES INFORMATIONS DE L'UTILISATEUR QUI A BADGE
    query  = ("SELECT badge_id FROM Utilisateur WHERE badge_id=%s ")
    
    cursor.execute(query, (id_user, ))
    rows = cursor.fetchall()
    rows = "".join(map(str,rows))
    print("rows: ", str(rows[2:-3]))
    print("badge: ", badge_id)
    if str(rows[2:-3])==id_user:
        print("existe")
        return True
    else:
        print("existe pas")
        return False


def ajout_tasse_sql(badge_id):
    
    conn = mysql.connector.connect(host="localhost",
                                   user="superuser", password="bonjour",
                                   database="Recup")
    cursor = conn.cursor()
    #IDENTIFICATION PAR BADGE DE L'UTILISATEUR

    id_user = badge_id[1:-1] #A REMPLACER PAR LA BADGEUSE

    #REQUETE DE RECUPERATION DES INFORMATIONS DE L'UTILISATEUR QUI A BADGE
    query  = ("SELECT * FROM Utilisateur WHERE badge_id=%s ")
    
    cursor.execute(query, (id_user, ))
    rows = cursor.fetchall()
    print(rows)
    for row in rows:
       #print('{0} : {1} - {2}'.format(row[0], row[1], row[2]))
       nb_tasses_empruntees = row[6] #Recuperation du nombre de tasses
       solde = row[7]  #Recuperation du solde

    if(nb_tasses_empruntees>0):
      new_nb_tasses_empruntees = nb_tasses_empruntees - 1 #Calcul du nombre total de tasses empruntees
      caution = 2 #Caution de 2€ rendue suite au depot

      #MODIFICATION DU NOMBRE DE TASSES EMPRUNTEES ET DU SOLDE DE L'UTILISATEUR
      solde = solde + caution
      solde = str(solde)
      new_nb_tasses_empruntees = str(new_nb_tasses_empruntees)
      sql = "UPDATE Utilisateur SET nb_tasses_empruntees = %s, solde=%s WHERE badge_id =%s"

      cursor.execute(sql, (new_nb_tasses_empruntees, solde, id_user)) #Cree une requete pour decrementer le nombre total de tasses empruntees  

      conn.commit() #Envoie la requête à la base de données
      conn.close()
      return True
    else:
        conn.close()
        return False

    
