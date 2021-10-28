const bRegistrar = document.getElementById("bRegistrar");

const nombre = document.getElementById("name");
const apellido = document.getElementById("surname");
const sexo = document.getElementById("sex");
const cumpleaños = document.getElementById("birthday");
const email = document.getElementById("email");
const usuario = document.getElementById("username");
const contraseña = document.getElementById("password");
const confirmarc = document.getElementById("pconfirmation");

const nWarning = document.getElementById("nameWarning");
const aWarning = document.getElementById("snameWarning");
const sWarning = document.getElementById("sexWarning");
const eWarning = document.getElementById("e-Warning");
const uWarning = document.getElementById("uWarning");
const cWarning = document.getElementById("pWarning");
const ccWarning = document.getElementById("pcWarning");

const today = new Date();

var month = today.getUTCMonth() + 1;
var day = today.getDate();
var year = today.getUTCFullYear();

maxdate = (year-18) + "-" + month + "-" + day;
mindate = (year-120) + "-" + month + "-" + day;

cumpleaños.value = maxdate;
cumpleaños.setAttribute("max", maxdate);
cumpleaños.setAttribute("min", mindate);

const e_regex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,3}$/;
const u_regex = /^([^0-9]*|[^a-z]*)$/;
const p_regex = /^([^0-9]*|[^A-Z]*|[^a-z]*)$/;

function warnings(input, warning, msg) {
    var x = true;
    if (input.value == "") {
        warning.textContent = msg;
        x = false;
    } else {warning.textContent = ""};
    return x;
}

function warning_matches(input, regex, warning, msg) {
    var x = true;
    if (!input.value.match(regex)) {
        warning.textContent = msg + ' no cumple con las caraterísticas. Intente nuevamente.';
        x = false;
    } else {warning.textContent = ""};
    return x;
}

function warning_wrongmatches(input, regex, warning, msg, min, max) {
    var x = true;
    if (input.value.match(regex) || input.value.length < min || input.value.length > max) {
        warning.textContent = msg + ' no cumple con las caraterísticas. Intente nuevamente.';
        x = false;
    } else {warning.textContent = ""};
    return x;
}

bRegistrar.addEventListener("click",function(evt){
    var registrar = false; var checked = true; var confirm = true;

    var nValidation = warnings(nombre, nWarning, 'Este campo es obligatorio');
    var aValidation = warnings(apellido, aWarning, 'Este campo es obligatorio');
    var sValidation = warnings(sexo, sWarning, 'Este campo es obligatorio');
    var ccValidation = warnings(confirmarc, ccWarning, 'Este campo es obligatorio');

    var uValidation = warning_wrongmatches(usuario, u_regex, uWarning, 'El usuario', 6, 30);
    var cValidation = warning_wrongmatches(contraseña, p_regex, cWarning, 'la contraseña', 8, 12);
    var eValidation = warning_matches(email, e_regex, eWarning, 'El correo electrónico');

    if(contraseña.value != "") { 
        if (confirmarc.value != contraseña.value) {
            ccWarning.textContent = 'Las contraseñas son distintas. Intente nuevamente.';
            confirm = false;
        };
    };

    if (nValidation && aValidation && sValidation && ccValidation && 
        uValidation && cValidation && eValidation && uValidation && cValidation && 
        checked && confirm){
            registrar = true;
    };

    if (registrar == false) {
        evt.preventDefault();
    } else {
        if (window.confirm('Esta seguro de querer registrar un ' + document.getElementById('userType').value)){
            return true;   
        } else { evt.preventDefault(); }
    }
})

function mostrarReq(id, script) {
    var userRequisito = document.getElementById(id);
    userRequisito.innerHTML = script;
}

function changeMargin(px) {
    const after = document.getElementsByClassName("aftersex");
    for (var i = 0; i < after.length; i++) {
        after[i].setAttribute("style", "margin-top: " + px);
    };
}

var ruta_img;
window.addEventListener('DOMContentLoaded', function () {
    var pimg = document.getElementById('peye');
    var pcimg = document.getElementById('pceye');
    var pwd = document.getElementById('password');
    var pwdc = document.getElementById('pconfirmation');

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