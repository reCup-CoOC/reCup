<?php

session_start();
include 'config.php';

$nb_tasses = $_SESSION['nb_tasses'];
$id_user = $_SESSION['id_users'];
$solde = $_SESSION['solde'];
$sNew_nb_tasses_empruntees = $_POST['new_nb_tasses_empruntees'];
$new_nb_tasses_empruntees = intval($sNew_nb_tasses_empruntees);
$new_nb_total_tasses = $new_nb_tasses_empruntees+$nb_tasses;


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
   <h2>Vous ne disposez pas d'assez d'argent pour acheter une boisson</h2><br/>
   <a href="index.php">Retour a l'accueil</a>
   <?php
}
?>
