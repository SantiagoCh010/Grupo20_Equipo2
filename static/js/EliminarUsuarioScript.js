const bEliminar = document.getElementById("bEliminar");

const usuario = document.getElementById("userName");
const contraseña = document.getElementById("password");
const email = document.getElementById("email");

const uWarning = document.getElementById("uWarning");
const cWarning = document.getElementById("pWarning");
const eWarning = document.getElementById("e-Warning");

const e_regex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,3}$/;

bEliminar.addEventListener("click",function(evt){
    if (window.confirm("¿Esta seguro de querer eliminar el usuario?")) {
        return true;
    } else {
        evt.preventDefault();
    }
})

function see_pword(eye, type){
    document.getElementById("peye").setAttribute("src", "{{ url_for('static', filename='" + eye + ".svg') }}");
    contraseña.setAttribute("type", type);
}

var ruta_img;
window.addEventListener('DOMContentLoaded', function () {
    var pimg = document.getElementById('peye');
    var pwd = document.getElementById('password');

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
})