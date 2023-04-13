let popup = document.getElementById("popup");
function openPopup(){
    popup.classList.add("open-popup");
}

function closePopup(){
    popup.classList.remove("open-popup");
}

function changeDevice(){
    var xhr = XMLHttpRequest();
    console.log('dsadsadsadsasa');
    xhr.onreadystatechange = function(){
        if(xhr.readyState == 4 && xhr.status == 200){
            var response = JSON.parse(xhr.responseText);
            console.log("I`m here");
            window.location.href = "https://http://127.0.0.1:8000/account/update/zxcv10";
        }
    };
    xhr.open("GET", "http://127.0.0.1:8000/account/update/zxcv10", true);
    xhr.send();
}