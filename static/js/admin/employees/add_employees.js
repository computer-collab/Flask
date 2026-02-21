RADIO = document.querySelectorAll(".radio-label");
let selectedRADIO;

document.getElementsByName("message").textContent = "window loaded";
RADIO.forEach((radio) => {
    radio.addEventListener("click", () => {
        if (selectedRADIO) {
            radio.forEach((r) => {
                r.classList.remove("selected");
            });
            document.getElementById("message").textContent = "";
        }