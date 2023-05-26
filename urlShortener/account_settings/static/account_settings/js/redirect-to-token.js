document.addEventListener("DOMContentLoaded", function() {
    var button = document.getElementById("select-all-points");
    button.addEventListener("click", function(){
        var form = document.getElementById("create-token-form");
        var canCreateField = document.getElementById('id_can_create');
        var canUpdateField = document.getElementById('id_can_update');
        var canArchiveField = document.getElementById('id_can_archive');
        canCreateField.checked = true;
        canArchiveField.checked = true;
        canUpdateField.checked = true;
    });
});

document.addEventListener("DOMContentLoader", function(){
    var createTokenBtn = document.getElementById("redirectLink");
    var modal = document.getElementById("modal-window");
    var modalIFrame = document.getElementById("modal-iframe");
    var closeBtn = document.querySelector(".close");

    createTokenBtn.addEventListener("click", function(){
        var newPageURL = "http://127.0.0.1:8080/account_settings/api/new/";
        modalIFrame.src = newPageURL;
        modal.style.display = "block";
    });
    closeBtn.addEventListener("click", function(){
        modal.style.display = "none";
        modalIFrame.src = ""
    });
});