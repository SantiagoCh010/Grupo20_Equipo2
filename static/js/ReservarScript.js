var bBuscar = document.getElementById("Buscar");
var bReservar = document.getElementById("bReservar");

const lOrigen = document.getElementById("lOrigen");
const lDestino = document.getElementById("lDestino");
const lPersona = document.getElementById("lPersona");

const origen = document.getElementById("origen");
const destino = document.getElementById("destino");
const fecha = document.getElementById("fecha");
const persona = document.getElementById("persona");

const today = new Date();

var month = today.getUTCMonth() + 1;
var day = today.getDate();
var year = today.getUTCFullYear();
date = year + "-" + month + "-" + day;
datemin = "2000-01-01";

fecha.value = date;
fecha.setAttribute("min", datemin);

function warnings(input, warning) {
    var x = true;
    if (input.value == "" || input.value < 0 || input.value == 0) {
        warning.style.visibility = "visible";
        warning.innerHTML = "Este campo es <br> obligatorio";
        x = false;
    } else {
        warning.style.visibility = "hidden";
        warning.innerText = "";
    }
    return x;
}

bBuscar.addEventListener("click", function(evt){
    var reservar = false;

    var oWarning = warnings(origen, lOrigen);
    var dWarning = warnings(destino, lDestino);
    var pWarning = warnings(persona, lPersona);

    if (oWarning && dWarning && pWarning) { reservar = true; }

    if (reservar == false) {
        console.log(evt);
        evt.preventDefault();
    } else {
        return true;
    }
})

bReservar.addEventListener("click", function(){
    if (window.confirm('¿Esta seguro de querer reservar este vuelo?')) {
        window.alert('El vuelo ha sido añadido a sus vuelos')
    }
})

