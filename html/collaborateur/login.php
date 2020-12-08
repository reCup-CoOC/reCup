<?php
if($_POST)
{
    include 'config.php';
    $nom=$_POST['nom']; //Stocker le resultat de la requete POST
    $prenom=$_POST['prenom'];
    $sNom=mysqli_real_escape_string($conn,$nom); //Enlever les caracteres d'echappement
    $sPrenom=mysqli_real_escape_string($conn,$prenom);
    // For Security
    $query="SELECT * From Collaborateur where nom='$sNom' and prenom='$sPrenom'"; //Definition de la requete vers BDD
    $result=mysqli_query($conn,$query);
    if(mysqli_num_rows($result)==1)
    {
        session_start();
        $_SESSION['anything']='something';
        $_SESSION['Nom_collab']= $sNom;
        $_SESSION['Prenom_collab']= $sPrenom;
        header('location:index.php');
    }
    else
    {
       echo "Vos credentials ne correspondent pas";
    }

}

?>

<form method="POST">
Nom:<br>
    <input type="text" name="nom"><br>
Prenom:<br>
    <input type="text" name="prenom"><br>
    <input type="submit">
</form>
