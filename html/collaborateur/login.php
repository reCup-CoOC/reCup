<?php
if($_POST)
{
    include 'config.php';
    $login=$_POST['login']; //Stocker le resultat de la requete POST
    $password=$_POST['password'];
    $sLogin=mysqli_real_escape_string($conn,$login); //Enlever les caracteres d'echappement
    $sPassword=mysqli_real_escape_string($conn,$password);
    // For Security
    $query="SELECT * From Collaborateur where login='$sLogin' and password='$sPassword'"; //Definition de la requete vers BDD
    $result=mysqli_query($conn,$query);
    if(mysqli_num_rows($result)==1)
    {
        session_start();
        $_SESSION['anything']='something';
        while ($ligne = mysqli_fetch_assoc($result))
        {
            $nom = $ligne['nom'];
            $prenom = $ligne['prenom'];
        }
        $_SESSION['Nom_collab']= $nom;
        $_SESSION['Prenom_collab']= $prenom;
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
    <input type="text" name="login"><br>
Prenom:<br>
    <input type="password" name="password"><br>
    <input type="submit">
</form>
