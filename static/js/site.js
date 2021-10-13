function alertaPiloto()
{
    alert("Si ya eres socio no necesitas crear una cuenta nueva. Inica Sesion con tus datos de siempre");
}

function verClave()
{
    console.log('Mostrar clave');

    var passWordInput = document.formularioRegistro.userPassword;
    passWordInput.type="text";
}

function ocultarClave()
{
    console.log('Ocultar clave');
    var passWordInput = document.formularioRegistro.userPassword;
    passWordInput.type="password";

    
}

function mostrarClave(){
    var cambio = document.getElementById("contraseña");
    if(cambio.type == "password"){
        cambio.type = "text";
        var miElto = document.getElementsByClassName("fa fa-eye-slash")[0];
        miElto.className = "fa fa-eye";
    }else{
        cambio.type = "password";
        var miElto = document.getElementsByClassName("fa fa-eye")[0];
        miElto.className = "fa fa-eye-slash";
    }
} 

function validarcontraseña() {
    var newPassword = document.getElementById("contraseña").value;
    var minNumberofChars = 8;
    var maxNumberofChars = 16;
    var regularExpression  = /^[a-zA-Z0-9!@#$%^&*]{6,16}$/;

    if(newPassword.length < minNumberofChars || newPassword.length > maxNumberofChars){
        return false;
    }

    if(!regularExpression.test(newPassword)) {
        alert("password should contain atleast one number and one special character");
        document.getElementById("login").disabled = true;
        return false;
    }
}

$(function () {
    $('#datetimepicker1').datetimepicker();
});
