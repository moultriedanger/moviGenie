document.querySelector(".submit_btn").addEventListener("click", function (event) {event.preventDefault();
    const form = document.getElementById("contactForm");
    const name = form.querySelector("#name").value.trim();
    const email = form.querySelector("#email").value.trim();
    const message = form.querySelector("#message").value.trim();
    const honeypot = form.querySelector("#importantdata").value.trim();

    if (!name || !email || !message) {
    alert("Please fill out all required fields.");
    return;
    }

    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailPattern.test(email)) {
    alert("Please enter a valid email address.");
    return;
    }

    const data = {
    name: name,
    email: email,
    comment: message,
    honeypot: honeypot,
    };

    const submitButton = event.target;

    fetch("http://127.0.0.1:5000/contact", {
    method: "POST",
    headers: {
        "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
    })
    .then((response) => {
        if (response.ok) {
        return response.text();
        } else {
        throw new Error("Network response was not ok");
        }
    })
    .then((data) => {
        alert("Form submitted successfully");
        submitButton.disabled = true;
        submitButton.style.backgroundColor = "rgba(126, 8, 27, 0.5)";
        submitButton.textContent = "Please wait";
        submitButton.classList.add("loading");
    })
    .catch((error) => {
        alert("Error submitting form");
    })
    .finally(() => {
        setTimeout(() => {
        submitButton.disabled = false;
        submitButton.style.backgroundColor = "";
        submitButton.textContent = "Submit";
        submitButton.classList.remove("loading");
        }, 10000);
    });
});