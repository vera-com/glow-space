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

// Sunday booking validation
const dateInput = document.getElementById("date");
const dateError = document.getElementById("date-error");

if (dateInput) {
    dateInput.addEventListener("change", function () {

        const selectedDate = new Date(this.value);

        if (selectedDate.getDay() === 0) {
            dateError.style.display = "block";
            this.value = "";
        } else {
            dateError.style.display = "none";
        }

    });
}
