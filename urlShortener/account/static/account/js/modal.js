let popup = document.getElementById("popup");
function openPopup(){
    popup.classList.add("open-popup");
}

function closePopup(){
    popup.classList.remove("open-popup");
}

var form = document.getElementById("code-form");
var button = document.getElementById("verify-button");
button.addEventListener('click', function(){
    form.submit();
});


$(document).ready(function() {
    $("#code-form").submit(function(event){
        event.preventDefault();

        $.ajax({
            type: "POST",
            url: "/input_code_form_view/",
            data: $(this).serialize(),
            success: function(response){
                console.log(response);
            },
            error: function(response){
                console.log(response);
            }
        });
    });
});

