<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Open+Sans&display=swap" rel="stylesheet">
    <script src="https://unpkg.com/sweetalert/dist/sweetalert.min.js"></script>
    <title>Calculadora php</title>
</head>
<body>
<div class="container">
        <h1>Calculadora php</h1>
        <hr>
        <form method="post">
            <label>Número 1</label>
            <input type="number" max=10000 min=0 name="numero1" placeholder="0" required autofocus>

            <label>Número 2</label>
            <input type="number" max=10000 min=0 name="numero2" placeholder="0" required >

            <hr>
            <input type="radio" class="form-check-input" name="opcion" value="sumar" required> Sumar
            <input type="radio" class="form-check-input" name="opcion" value="restar" required> Restar
            <input type="radio" class="form-check-input" name="opcion" value="multiplicar" required> Multiplicar
            <input type="radio" class="form-check-input" name="opcion" value="division" required> Division
            <input type="radio" class="form-check-input" name="opcion" value="potenciacion" required> Potenciacion
            <input type="radio" class="form-check-input" name="opcion" value="concatenacion" required> Concatenacion 
            <hr>
            <input type="submit" class="btn btn-success w-25" value="Enviar">
            <input type="reset" class="btn btn-danger w-25" value="Limpiar">
            <hr>
        </form>
    </div>
    <div class="container">
    <?php
        if($_POST){
            function Sumar (){
                echo "La suma de los números es: ".($_POST['numero1']+$_POST['numero2']);
            }

            function Restar (){
                echo "La resta de los números es: ".($_POST['numero1']-$_POST['numero2']);
            }

            function Multiplicar (){
                echo "La multiplicación de los números es: ".($_POST['numero1']*$_POST['numero2']);
            }

            function Division (){
                if ($_POST['numero2']==0)
                    $d="Error: division por 0";
                else 
                    $d=$_POST['numero1']/$_POST['numero2'];
                    echo "La divison de los números es: ".$d;
            }

            function Potenciacion (){
                echo "La potenciacion de los números es: ".(pow($_POST['numero1'],$_POST['numero2']));
            }

            function Concatenacion (){
                echo "La Concatenación de los números es: ".($_POST['numero1'].$_POST['numero2']);
            }
            switch($_POST['opcion']){
                case 'sumar':
                    Sumar();
                    break;
                case 'restar':
                    Restar();
                    break;
                case 'multiplicar':
                    Multiplicar();
                    break;
                case 'division':
                    Division();
                    break;
                case 'potenciacion':
                    Potenciacion();
                    break;
                case 'concatenacion':
                    Concatenacion();
                    break;
                default:
                    echo "Error en la opción seleccionada";
                    break;
            }

        }
?>
    </div>
</body>
</html>