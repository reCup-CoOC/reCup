<?php
// first thing is to start session
session_start();
// now to check if variable is true


if(!$_SESSION['anything'])
{
    header('location:login.php');
}

//Utilisateur connecté

$id_user = $_SESSION['id_users'];

include 'config.php';

$query="SELECT nb_tasses_empruntees,solde From Utilisateur where ID_USERS='$id_user'";

if ($result = mysqli_query($conn,$query))
{
  while ($ligne = mysqli_fetch_assoc($result))
  {
      $nb_total_tasses = $ligne['nb_tasses_empruntees'];
      $solde = $ligne['solde'];
  }
}
  $caution = 2*$nb_total_tasses;

  ?>
  <h1>Bienvenue <?php echo $_SESSION['Prenom_user']; ?> <?php echo $_SESSION['Nom_user']; ?> ID : <?php echo $id_user; ?></h1>
  <p>Nombre de tasses empruntées : <?php echo $nb_total_tasses; ?></p>
  <p>Caution actuellement prélevée : <?php echo $caution; ?> €</p>

<a href="logout.php">Logout</a>
