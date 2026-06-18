const menuToggle = document.getElementById("menu-toggle");
const navLinks = document.getElementById("nav-links");
const navItems = document.querySelectorAll(".nav-links a");

if (menuToggle && navLinks) {
    menuToggle.addEventListener("click", function () {
        navLinks.classList.toggle("active");
    });

    navItems.forEach(function (link) {
        link.addEventListener("click", function () {
            navLinks.classList.remove("active");
        });
    });
}