const bEditar = document.getElementById("bEditar");

const piloto = document.getElementById("pilotName");
const IDpiloto = document.getElementById("pilotID");
const IDavion = document.getElementById("airplane");

const pWarning = document.getElementById("npWarning");
const ipWarning = document.getElementById("cpWarning");
const iaWarning = document.getElementById("capWarning");

function replace(input) {
    if (input.value == ""){
        input.value = input.placeholder;
    }
}

bEditar.addEventListener("click", function(evt){
    replace(piloto);
    replace(IDavion);
    replace(IDpiloto);

    if (window.confirm("¿Esta seguro de editar el vuelo?")) {
        return true;
    } else {
        evt.preventDefault();
    }
})