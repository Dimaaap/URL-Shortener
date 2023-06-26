const form = document.getElementById("shortened-url-form");
const urlField = document.getElementById("id_user_url");
let url = urlField.value;
console.log(url);
let visitButton = document.getElementById("visit-url");
visitButton.addEventListener('click', function(){
    window.location.href = url;
})
