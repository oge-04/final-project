function login() {
    let email = "admin@admin.com";
    let password = "admin123";
    let loginEmail = document.getElementById("loginEmail").value;
    let loginPassword = document.getElementById("loginPassword").value;

    console.log("Entered Email: ", loginEmail);
    console.log("Entered Password: ", loginPassword);

    if (loginEmail === email && loginPassword === password) {
        alert("Login Successful");
        window.location.assign('./products.html');
    } else {
        alert("Incorrect Email or Password");
    }
}

