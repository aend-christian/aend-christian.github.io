

/* Nav Toggle Open and Close Function */
function showNav() {
    var NavMenu = document.getElementById("nav-menu");
    
    if (NavMenu.style.display === "none") {
        NavMenu.style.display = "block";
    }
    else {
        NavMenu.style.display = "none";
    }
}
