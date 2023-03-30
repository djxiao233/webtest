function myFunction() {
    var box = document.getElementById("smallblock");
    box.mousedown(function () {
        box.style.backgroundColor = "red";
    });
    box.mouseup(function () {
        box.style.backgroundColor = "yellow";
    });
}