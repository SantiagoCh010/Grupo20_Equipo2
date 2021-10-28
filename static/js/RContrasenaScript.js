const bRecuperar = document.getElementById("bRecuperar");

const usuario = document.getElementById("userName");
const correo = document.getElementById("email");

const uWarning = document.getElementById("uWarning");
const cWarning = document.getElementById("e-Warning");

const e_regex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,3}$/;

function warnings(input, warning, msg, min, max) {
    var x = true;
    if (input.value == "") {
        warning.textContent = 'Este campo es obligatorio';
        x = false;
    } else {
        if (input.value.length < min || input.value.length > max) {
        warning.textContent = msg + ' no cumple con las caraterísticas. Intente nuevamente.';
        x = false;
        } else {
        warning.textContent = ""};
    }
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

bRecuperar.addEventListener("click",function(evt){
    var recuperar = false;

    var uValidation = warnings(usuario, uWarning, 'El usuario', 6, 30);
    var cValidation = warnings(correo, cWarning, 'El correo electrónico', 4, 150);

    if (!cValidation) {} 
    else {var cValidation = warning_matches(correo, e_regex, cWarning, 'El correo electrónico');}

    if (uValidation && cValidation){
        recuperar = true;
    };

    if (recuperar == false) {
        console.log(evt);
        evt.preventDefault();
    } else {
        return true;
    }
})

function see_pword(eye, type){
    document.getElementById("peye").setAttribute("src", "{{ url_for('static', filename='" + eye + ".svg') }}");
    contraseña.setAttribute("type", type);
}