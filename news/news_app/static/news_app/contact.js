function check() {
    var a = document.getElementById("name");
    var b = document.getElementById("textarea");
    var c = document.getElementById("mob");
    var d = document.getElementById("email");
    if (a.value.trim() == "" || b.value.trim() == "" || c.value.trim() == "" || d.value.trim() == "") {
        alert("Fill the required field");
        return false;
    }
    else if (a.value.length < 3) {
        alert("Name cannot be too short (must contain atleast 3 characters)");
        return false;
    } else if (b.value.length < 10) {
        alert("Description cannot be too short (must contain atleast 10 characters)");
        return false;
    } else {
        alert("Your response is received")
    }
}