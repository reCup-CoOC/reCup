<?php
// first thing is to start session
session_start();
// now to check if variable is true


if(!$_SESSION['anything'])
{
    header('location:login.php');
}


//Utilisateur connecté

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
    echo "Nombre de tasse empruntées : ";
    echo $nb_total_tasses;
}

?>
<br/><br/><a href="logout.php">Logout</a>
