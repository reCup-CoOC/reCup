<?php

session_start();
?>
<h2>Vous êtes un : </h2>
<form action=./utilisateur/index.php method="POST">
    <input type="submit" value="utilisateur">
</form>

<form action=./collaborateur/index.php method="POST">
    <input type="submit" value="collaborateur">
</form>

<h2>Quel simulateur voulez-vous utiliser?</h2>
<form action=./simulation_utilisateur/index.php method="POST">
    <input type="submit" value="Utilisateur">
</form>
