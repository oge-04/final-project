function login() {
    let email = "admin@admin.com";
    let password = "admin123";
    let loginEmail = document.getElementById("loginEmail").value;
    let loginPassword = document.getElementById("loginPassword").value;

    if (loginEmail === email && loginPassword === password) {
        alert("Login Successful");
        window.location ="products.html";
    } else {
        alert("Incorrect Email or Password");
    }
}

