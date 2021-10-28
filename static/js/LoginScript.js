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