var modalOpen = false;

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

document.getElementById('create-token-form').addEventListener('submit', function(event){
    event.preventDefault();
    var formData = new FormData(this);
    var xhr = new XMLHttpRequest();
    xhr.open('POST', this.action);
    xhr.setRequestHeader('X-CSRFToken', formData.get('csrfmiddlewaretoken'));
    xhr.onload = function(){
        if (xhr.status === 200){
            localStorage.setItem("showModal", "true");
            window.location.reload();
        }
    };
    xhr.send(formData);
});

window.addEventListener('load', function(){
    if(localStorage.getItem("showModal")){
        localStorage.removeItem("showModal");
        var modal = document.getElementById('modal-token');
        modal.style.display = 'block';
        modalOpen = true;
        modal.style.display = 'flex';
        modal.addEventListener('touchmove', preventScroll, {passive: false});
        modal.addEventListener('wheel', preventScroll, {passive: false});
    }
});


function preventScroll(event){
    event.stopPropagation();
}

var closeBtn = document.getElementById("close-modal");
var modal = document.getElementById("modal-token");
function closeModal(){
    modal.style.display = 'none';
    document.body.classList.remove('modal-open');
    modalOpen = false;
    modal.removeEventListener('touchmove', preventScroll);
    modal.removeEventListener('wheel', preventScroll);
}

closeBtn.addEventListener('click', closeModal)
