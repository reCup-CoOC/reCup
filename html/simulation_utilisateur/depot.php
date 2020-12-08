<?php

session_start();
include 'config.php';

$nb_tasses = $_SESSION['nb_tasses'];
$id_user = $_SESSION['id_users'];
$solde = $_SESSION['solde'];
$sNew_nb_tasses_deposees = $_POST['new_nb_tasses_deposees'];
$new_nb_tasses_deposees = intval($sNew_nb_tasses_deposees);
$new_solde = $solde+(2*$new_nb_tasses_deposees);

if($nb_tasses>=$new_nb_tasses_deposees)
{
   $nb_final_tasses = $nb_tasses-$new_nb_tasses_deposees;
   $query="UPDATE Utilisateur SET nb_tasses_empruntees = '$nb_final_tasses', solde='$new_solde' WHERE ID_USERS='$id_user'";
   if(mysqli_query($conn,$query))
   {
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
   echo "Vous ne disposez pas d'autant de tasses";
   ?>
   <br/>
   <a href="index.php">Retour à l'accueil</a>
   <?php
}

?>
