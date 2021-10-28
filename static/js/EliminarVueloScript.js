const bEliminar = document.getElementById("bEliminar");

const date = document.getElementById("departure-D");
const hour = document.getElementById("departure-H");
const IDplane = document.getElementById("airplane");
const comment = document.getElementById("comentario");  

const dWarning = document.getElementById("dDWarning");
const hWarning = document.getElementById("dHWarning");
const capWarning = document.getElementById("capWarning");
const mEWarning = document.getElementById("mEWarning");

function warnings(input, warning) {
    var x = true;
    if (input.value == "") {
        warning.textContent = "Este campo es obligatorio";
        x = false;
    } else {warning.textContent = ""};
    return x;
}

bEliminar.addEventListener("click",function(evt){
    var eliminar = false;

    var dValitadion = warnings(date, dWarning);
    var hValidation = warnings(hour, hWarning);
    var capValidation = warnings(IDplane, capWarning);
    var mEValidation = warnings(comment, mEWarning);

    if(dValitadion && hValidation && 
       capValidation && mEValidation) 
    { eliminar = true; }

    if (eliminar) {
        if (window.confirm("¿Esta seguro de querer eliminar el usuario?")) {
            return true;
        } else {
            evt.preventDefault();
        }
    } else {
        evt.preventDefault();
    }

})