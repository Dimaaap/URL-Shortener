$(document).ready(function(){
    $("#my-modal").modal('show');
});

$(document).ready(function(){
    $("#my-modal .close, #myModal .modal-footer button").click(function(){
        $("#my-modal").modal('hide');
    });
});