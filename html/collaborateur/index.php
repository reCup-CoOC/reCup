<?php
// first thing is to start session
session_start();
// now to check if variable is true


if(!$_SESSION['anything'])
{
    header('location:login.php');
}


//Utilisateur connecté

?>
<h2>Bienvenue <?php echo $_SESSION['Prenom_collab']; ?> <?php echo $_SESSION['Nom_collab']; ?></h2>
<?php

include 'config.php';

$query="SELECT nom, prenom, nb_tasses_empruntees From Utilisateur where nb_tasses_empruntees > 0";
if ($result = mysqli_query($conn,$query))
{
    echo "Listes des utilisateurs n'ayant pas rendu leur tasse :";
    ?><br/><?php
    while ($ligne = mysqli_fetch_assoc($result))
    {
       $nom_utilisateur = $ligne['nom'];
       $prenom_utilisateur = $ligne['prenom'];
       $nb_tasses_utilisateur = $ligne['nb_tasses_empruntees'];
       $nb_total_tasses += $nb_tasses_utilisateur;
       ?>
       <table>
           <tr>
              <td><?php echo $nom_utilisateur; ?> </td>
              <td><?php echo $prenom_utilisateur; ?> </td>
              <td><?php echo $nb_tasses_utilisateur; ?> </td>
           </tr>
       </table>

       <?php
    }
    ?><br/><?php
    echo "Nombre total de tasse empruntées : ";
    echo $nb_total_tasses;
}
?>
<!--Code HTML du bouton Emprunter une tasse-->

<br/><br/>
<p>Emprunt de tasse pour les consommateurs</p>

  <form action=emprunt.php method="POST">
     <p>ID du consommateur :
        <input type"number" name="id_consumer"><br/>
     </p>
     <p>Combien de tasses souhaitez-vous emprunter pour ce consommateur ? :
        <input type"number" name="new_nb_tasses_empruntees"><br/>
     </p>
     <input type="submit" value="Emprunter">
  </form>



<br/><br/><a href="logout.php">Logout</a>
