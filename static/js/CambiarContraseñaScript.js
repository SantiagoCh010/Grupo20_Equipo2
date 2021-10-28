const bCambiar = document.getElementById("bCambiar");

const antigua = document.getElementById("npassword");
const nueva = document.getElementById("password");
const confirmacion = document.getElementById("cpassword");

const npWarning = document.getElementById("npWarning");
const pWarning = document.getElementById("pWarning");
const pcWarning = document.getElementById("pcWarning");

const p_regex = /^([^0-9]*|[^A-Z]*|[^a-z]*)$/;

function warning_wrongmatches(input, regex, warning, msg, min, max) {
    var x = true;
    if (input.value == "") {
        warning.textContent = 'Este campo es obligatorio';
        x = false;
    } else {
        if(input.value.match(regex) || input.value.length < min || input.value.length > max){
            warning.textContent = msg + ' no cumple con las caraterísticas. Intente nuevamente.';
            x = false;
        } else {
            warning.textContent = ""
        }
    };
    return x;
}

bCambiar.addEventListener("click", function(evt){
    var cambiar = false; var confirm = true;

    var npValidation = warning_wrongmatches(nueva, p_regex, pWarning, 'la contraseña', 8, 12);
    var pValidation = warning_wrongmatches(antigua, p_regex, npWarning, 'la contraseña', 8, 12);
    var pcValidation = warning_wrongmatches(confirmacion, p_regex, pcWarning, 'la contraseña', 8, 12);

    if(nueva.value != "") { 
        if (confirmacion.value != nueva.value) {
            pcWarning.textContent = 'Las contraseñas son distintas. Intente nuevamente.';
            confirm = false;
        };
    };

    if (npValidation && pValidation && pcValidation && confirm){
        cambiar = true;
    };

    if (cambiar == false) {
        console.log(evt);
        evt.preventDefault();
    } else {
        return true;
    }
})

function mostrarReq(id, script) {
    var userRequisito = document.getElementById(id);
    userRequisito.innerHTML = script;
}

var ruta_img;
window.addEventListener('DOMContentLoaded', function () {
    var npimg = document.getElementById('npeye');
    var pimg = document.getElementById('peye');
    var pcimg = document.getElementById('pceye');
    var npwd = document.getElementById('npassword');
    var pwd = document.getElementById('password');
    var pwdc = document.getElementById('cpassword');

    npimg.addEventListener('mouseover', (event) => {
        var rimg = document.getElementById('hiPassword')
        npwd.type = "text";
        ruta_img = npimg.src;
        npimg.src = rimg.value;
    });

    npimg.addEventListener('mouseout', (event) => {
        npwd.type = "password";
        npimg.src = ruta_img;
    });
    
    pimg.addEventListener('mouseover', (event) => {
        var rimg = document.getElementById('hiPassword')
        pwd.type = "text";
        ruta_img = pimg.src;
        pimg.src = rimg.value;
    });

    pimg.addEventListener('mouseout', (event) => {
        pwd.type = "password";
        pimg.src = ruta_img;
    });

    pcimg.addEventListener('mouseover', (event) => {
        var rimg = document.getElementById('hiCPassword')
        pwdc.type = "text";
        ruta_img = pcimg.src;
        pcimg.src = rimg.value;
    });

    pcimg.addEventListener('mouseout', (event) => {
        pwdc.type = "password";
        pcimg.src = ruta_img;
    });
})