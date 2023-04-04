//$(document).ready(function(){
/*    $("#my-modal").modal('show');
});

$(document).ready(function(){
    $("#my-modal .close, #myModal .modal-footer button").click(function(){
        $("#my-modal").modal('hide');
    });
});*/

let popup = document.getElementById("popup");
function openPopup(){
    popup.classList.add("open-popup");
}

function closePopup(){
    popup.classList.remove("open-popup");
}