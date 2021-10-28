const bEditar = document.getElementById("bEditar");

const nombre = document.getElementById("name");
const apellido = document.getElementById("surname");
const sexo = document.getElementById("sex");
const cumpleaños = document.getElementById("birthday");
const email = document.getElementById("email");
const usuario = document.getElementById("username");

const uWarning = document.getElementById("uWarning");
const cWarning = document.getElementById("e-Warning");

const today = new Date();

var month = today.getUTCMonth() + 1;
var day = today.getDate();
var year = today.getUTCFullYear();
maxdate = (year-18) + "-" + month + "-" + day;

cumpleaños.setAttribute("max", maxdate);

const e_regex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,3}$/;
const u_regex = /^([^0-9]*|[^a-z]*)$/;

function warnings(input, warning, regex, msg, min, max) {
    var x = true;
    if (!input.value.match(regex) || input.value.length < min || input.value.length > max) {
        warning.textContent = msg + ' no cumple con las caraterísticas. Intente nuevamente.';
        x = false;
    } else {
        warning.textContent = ""};
    return x;
}

var loadFile = function (event) {
    var image = document.getElementById("profile-pic");
    image.src = URL.createObjectURL(event.target.files[0]);
};

function replace(input) {
    if (input.value == ""){
        input.value = input.placeholder;
    }
}

function warning_wrongmatches(input, regex, warning, msg, min, max) {
    var x = true;
    if (input.value.match(regex) || input.value.length < min || input.value.length > max) {
        warning.textContent = msg + ' no cumple con las caraterísticas. Intente nuevamente.';
        x = false;
    } else {warning.textContent = ""};
    return x;
}

bEditar.addEventListener("click", function(evt){
    var editar = false;

    replace(nombre);
    replace(apellido);
    replace(sexo);
    replace(email);
    replace (usuario)

    var uValidation = warning_wrongmatches(usuario, u_regex, uWarning, 'El usuario', 6, 30);
    var cValidation = warnings(email, cWarning, e_regex, 'El correo electrónico', 4, 150);

    if (uValidation && cValidation) {editar = true}

    if (editar == false) {
        console.log(evt);
        evt.preventDefault();
    } else {
        if (window.confirm("¿Esta seguro de editar el usuario?")) {
            return true;
        } else {
            evt.preventDefault();
        }
    }
})

function mostrarReq(id, script) {
    var userRequisito = document.getElementById(id);
    userRequisito.innerHTML = script;
}

sexo.value = document.getElementById("sexo").value;