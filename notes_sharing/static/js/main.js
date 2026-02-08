// Navbar shadow on scroll
window.addEventListener("scroll", () => {
    const navbar = document.querySelector(".navbar");
    if (!navbar) return;
    navbar.classList.toggle("shadow", window.scrollY > 20);
});

// Dark mode toggle
const toggleTheme = () => {
    const html = document.documentElement;
    const theme = html.getAttribute("data-theme") === "dark" ? "light" : "dark";
    html.setAttribute("data-theme", theme);
    localStorage.setItem("theme", theme);
};

// Load saved theme
document.addEventListener("DOMContentLoaded", () => {
    const savedTheme = localStorage.getItem("theme");
    if (savedTheme) {
        document.documentElement.setAttribute("data-theme", savedTheme);
    }
});

// Live search (notes)
const searchInput = document.getElementById("searchInput");
if (searchInput) {
    searchInput.addEventListener("keyup", function () {
        const query = this.value.toLowerCase();
        document.querySelectorAll(".note-card").forEach(card => {
            card.style.display = card.innerText.toLowerCase().includes(query)
                ? "block"
                : "none";
        });
    });
}

// Password toggle
document.querySelectorAll(".toggle-password").forEach(btn => {
    btn.addEventListener("click", () => {
        const input = document.getElementById(btn.dataset.target);
        input.type = input.type === "password" ? "text" : "password";
    });
});
