var bMandar = document.getElementById("bMandar")

var star1 = document.getElementById("rate-1");
var star2 = document.getElementById("rate-2");
var star3 = document.getElementById("rate-3");
var star4 = document.getElementById("rate-4");
var star5 = document.getElementById("rate-5");

bMandar.addEventListener("click", function(evt){

    if (star1.checked == true || star2.checked == true || star3.checked == true ||
        star4.checked == true || star5.checked == true) {
        if (document.getElementById("textarea").value == ""){
            if (!window.confirm("¿Está seguro de no querer dejar un comentario?")){
                evt.preventDefault();
            }
        }
    } else {
        window.alert("Para mardar hay que marcar una calificación");
        evt.preventDefault();
    }
})