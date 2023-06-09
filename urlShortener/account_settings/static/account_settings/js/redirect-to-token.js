var modalOpen = false;


// Реалізація роботи кнопки Select All та Unselect All
document.addEventListener("DOMContentLoaded", function() {
    var button = document.getElementById("select-all-points");
    var isAllSelected = false;
    button.addEventListener("click", function(){
        var form = document.getElementById("create-token-form");
        var canCreateField = document.getElementById('id_can_create');
        var canUpdateField = document.getElementById('id_can_update');
        var canArchiveField = document.getElementById('id_can_archive');
        if (!isAllSelected){
            canCreateField.checked = true;
            canArchiveField.checked = true;
            canUpdateField.checked = true;
            button.innerText = '(Unselect All)';
            isAllSelected = true;
        }
        else{
            canCreateField.checked = false;
            canArchiveField.checked = false;
            canUpdateField.checked = false;
            button.innerText = '(Select All)';
            isAllSelected = false;
        }
    });
});

//Перезавантаження сторінки після створення API-ключа
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
var overlay = document.getElementById('overlay');

//Відкриття модального вікна
window.addEventListener('load', function(){
    if(localStorage.getItem("showModal")){
        localStorage.removeItem("showModal");
        var modal = document.getElementById('modal-token');
        overlay.style.display = 'block';
        modalOpen = true;
        modal.style.display = 'flex';
        document.body.style.overflow = 'hidden';
    }
});


var closeBtn = document.getElementById("close-modal");
var modal = document.getElementById("modal-token");
function closeModal(){
    modal.style.display = 'none';
    overlay.style.display = 'none';
    document.body.classList.remove('modal-open');
    modalOpen = false;
    document.body.style.overflow = 'auto';
}

closeBtn.addEventListener('click', closeModal)

