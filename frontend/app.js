const BASE_URL = "http://127.0.0.1:8000";

// SIGNUP
async function signup() {
    const email = document.getElementById("signup_email").value;
    const password = document.getElementById("signup_password").value;

    const res = await fetch(`${BASE_URL}/signup`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email, password })
    });

    const data = await res.json();
    alert(data.message);
}

// LOGIN
async function login() {
    const email = document.getElementById("login_email").value;
    const password = document.getElementById("login_password").value;

    const res = await fetch(`${BASE_URL}/login`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email, password })
    });

    const data = await res.json();

    if (data.token) {
        localStorage.setItem("token", data.token);
        window.location.href = "dashboard.html";
    } else {
        alert("Invalid login");
    }
}

// ADD PASSWORD
async function addPassword() {
    const token = localStorage.getItem("token");
    const site = document.getElementById("site").value;
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    await fetch(`${BASE_URL}/add-password`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + token
        },
        body: JSON.stringify({ site, username, password })
    });

    loadPasswords();
}

// GET PASSWORDS
async function loadPasswords() {
    const token = localStorage.getItem("token");

    const res = await fetch(`${BASE_URL}/get-passwords`, {
        headers: { "Authorization": "Bearer " + token }
    });

    const data = await res.json();
    const table = document.getElementById("passwordTable");
    table.innerHTML = "";

    data.forEach(p => {
        table.innerHTML += `
            <tr>
                <td>${p.site}</td>
                <td>${p.username}</td>
                <td>${p.password}</td>
            </tr>
        `;
    });
}
function copy(text) {
    navigator.clipboard.writeText(text);
    alert("Password copied!");
}


// Auto-load when dashboard opens
if (window.location.pathname.includes("dashboard.html")) {
    loadPasswords();
}