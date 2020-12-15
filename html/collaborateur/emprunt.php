<?php

session_start();
include 'config.php';

$id_user = $_POST['id_consumer'];

$query2="SELECT nb_tasses_empruntees, solde From Utilisateur where ID_USERS='$id_user'";
if ($result2 = mysqli_query($conn,$query2))
{
  while ($ligne2 = mysqli_fetch_assoc($result2))
  {
      $nb_total_tasses = $ligne2['nb_tasses_empruntees'];
      $solde = $ligne2['solde'];
  }
}
else
{
  echo "Erreur lors de la requête: " . mysqli_error($conn);
}

$sNew_nb_tasses_empruntees = $_POST['new_nb_tasses_empruntees'];
$new_nb_tasses_empruntees = intval($sNew_nb_tasses_empruntees);
$new_nb_total_tasses = $new_nb_tasses_empruntees+$nb_total_tasses;


if($solde >= (2*$new_nb_tasses_empruntees))
{
   $new_solde = $solde - (2*$new_nb_tasses_empruntees);  
   $query="UPDATE Utilisateur SET nb_tasses_empruntees = '$new_nb_total_tasses', solde='$new_solde' WHERE ID_USERS='$id_user'";
   if (mysqli_query($conn,$query))
   {
      echo "";
      echo "Record updated successfully";
      header('location:logout.php');
   }
   else
   {
      echo "Error updating record: " . mysqli_error($conn);
   }
}
else
{
   ?>
   <h2>L'utilisateur n'a pas d'assez d'argent pour acheter une boisson</h2><br/>
   <a href="index.php">Retour a l'accueil</a>
   <?php
}
?>
