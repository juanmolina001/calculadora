function enviar(){
    var contenido =document.querySelector('#contenido')
    var v1 =document.querySelector('#t1').value
    var v2 =document.querySelector('#v2').value
    var url=''
    if (document.querySelector('#opcion1').cheched)
        url='http://127.0.0.1:5000/'+v1+'/'+v2
    else if(document.querySelector('#opcion2').cheched)
        url='http://127.0.0.1:5000/resta/'+v1+'/'+v2
    else if(document.querySelector('#opcion3').checked)
        url='http://127.0.0.1:5000/multiplicacion/'+v1+'/'+v2
    else if(document.querySelector('#opcion4').checked)
        url='http://127.0.0.1:5000/division/'+v1+'/'+v2
    else if(document.querySelector('#opcion5').checked)
        url='http://127.0.0.1:5000/potenciacion/'+v1+'/'+v2
    else if(document.querySelector('#opcion6').checked)
        url='http://127.0.0.1:5000/seno/'+v1
    else if(document.querySelector('#opcion7').checked)
        url='http://127.0.0.1:5000/coseno/'+v1
    else
        swal("Mensaje", "Seleccione una opción", "warning");
    

    fetch(url)
    .then (function(response){
        if (response.ok){
            return response.json()
        }else{
            throw "Error en la llamada"
        }
    })

    .then(function(texto){
        console.log(texto)
        cadena="<h3> Resultado: "+texto.resultado+" Operacion: "+texto.Operacion+"</h3>"
        contenido.innerHTML=`${cadena}`
        //swal("Mensaje", "Proceso realizado correctamente", "success");

    })

    .catch(function(Error){
        console.log(Error)
        swal(Error)
        swal({
            title: "Advertencia",
            text: Error,
            icon: "warning",
            buttons: true,
            dangerMode: true
        })
    })
        
}