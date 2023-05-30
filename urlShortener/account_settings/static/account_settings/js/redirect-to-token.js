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
            var modal = document.getElementById('modal-token');
            modal.style.display = 'block';
        }
    };
    xhr.send(formData);
});

var modal = document.getElementById('modal-token');
modal.style.display = 'block';
document.body.classList.add('modal-open');