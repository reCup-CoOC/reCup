<?php
if($_POST)
{
    include 'config.php';
    $login=$_POST['login']; //Stocker le resultat de la requete POST
    $password=$_POST['password'];
    $sLogin=mysqli_real_escape_string($conn,$login); //Enlever les caracteres d'echappement
    $sPassword=mysqli_real_escape_string($conn,$password);
    // For Security
    $query="SELECT * From Utilisateur where login='$sLogin' and password='$sPassword'"; //Definition de la requete vers BDD
    $result=mysqli_query($conn,$query);
    if(mysqli_num_rows($result)==1)
    {
        session_start();
        $_SESSION['anything']='something';
        $_SESSION['Nom_user']= $sNom;
        $_SESSION['Prenom_user']= $sPrenom;
        while ($ligne = mysqli_fetch_assoc($result))
        {
           $nom = $ligne['nom'];
           $prenom = $ligne['prenom'];
           $id_user =  $ligne['ID_USERS'];
           $nb_tasses = $ligne['nb_tasses_empruntees'];
        }
        
        $_SESSION['Nom_user']= $nom;
        $_SESSION['Prenom_user']= $prenom;
        $_SESSION['id_users'] = $id_user;
        $_SESSION['nb_tasses'] = $nb_tasses;
        header('location:index.php');
    }
    else
    {
       echo "Vos credentials ne correspondent pas";
    }

}

?>

<form method="POST">
Login:<br>
    <input type="text" name="login"><br>
Password:<br>
    <input type="password" name="password"><br>
    <input type="submit">
</form>

