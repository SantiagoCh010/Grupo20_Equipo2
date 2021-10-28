var bBuscar = document.getElementById("Buscar");

const lOrigen = document.getElementById("lOrigen");
const lDestino = document.getElementById("lDestino");
const lFecha = document.getElementById("lFecha")
const lVuelo = document.getElementById("lVuelo")

const origen = document.getElementById("origen");
const destino = document.getElementById("destino");
const fecha = document.getElementById("fecha");
const vuelo = document.getElementById("IDVuelo")

function warnings(input, warning, msg) {
    var x = true;
    if (input.value == "" || input.value == msg) {
        warning.style.visibility = "visible";
        warning.innerHTML = "Este campo es <br> obligatorio";
        x = false;
    } else {
        warning.style.visibility = "hidden";
        warning.innerText = "";
    }
    console.log(x);
    return x;
}

function validar(input1, input2, input3, warning2, warning3){
    if (input1.value != "" && input2.value == ""){
        var city = warnings(input2, warning2, "");
        lVuelo.style.visibility = "hidden";
        return city;
    }
    if (input1.value != "" && input3.value == ""){
        var date = warnings(input3, warning3, "");
        lVuelo.style.visibility = "hidden";
        return date;
    }
    return null;
}

bBuscar.addEventListener("click", function(evt){
    var consultar = true;

    if (origen.value != "" || destino.value != "" || fecha.value != "") {
        vuelo.value = "";
        lVuelo.style.visibility = "hidden";
    }
    if (vuelo.value != ""){
        origen.value = destino.value = fecha.value = "";
    }
    if (origen.value == "" && destino.value == "" && fecha.value == ""){
        consultar = warnings(vuelo, lVuelo, "#");
        lOrigen.style.visibility = lDestino.style.visibility = lFecha.style.visibility = "hidden";
    }

    oValidation = validar(origen, destino, fecha, lDestino, lFecha);
    dValidation = validar(destino, origen, fecha, lOrigen, lFecha);

    if (oValidation != null) {consultar = oValidation}; if (dValidation != null) {consultar = dValidation};

    if (consultar) {
        return true;
    } else {
        evt.preventDefault();
    }
})