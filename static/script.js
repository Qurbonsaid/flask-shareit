function isSelected() {
    var files = document.getElementById("files");
    if (files.value != "") {
        document.getElementById("submit_button").disabled = false;
    }
}