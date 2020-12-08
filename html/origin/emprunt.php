<?php

session_start();
include 'config.php';

$nb_tasses = $_SESSION['nb_tasses'];
$id_user = $_SESSION['id_users'];
$sNew_nb_tasses_empruntees = $_POST['new_nb_tasses_empruntees'];
$new_nb_tasses_empruntees = intval($sNew_nb_tasses_empruntees);
$new_nb_total_tasses = $new_nb_tasses_empruntees+$nb_tasses;

echo "Le nombre de tasses à emprunter est : ";
echo $new_nb_tasses_empruntees;

$query="UPDATE Utilisateur SET nb_tasses_empruntees = '$new_nb_total_tasses' WHERE ID_USERS='$id_user'";
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

?>

