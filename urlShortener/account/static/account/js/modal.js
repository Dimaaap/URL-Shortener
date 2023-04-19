let popup = document.getElementById("popup");
function openPopup(){
    popup.classList.add("open-popup");
}

function closePopup(){
    popup.classList.remove("open-popup");
}

document.getElementById("openCodesButton").addEventListener("click", function(){
    document.getElementById("codesModal").classList.add("open")
})

//Закриття модального вікна
document.getElementById("closeCodesButton").addEventListener("click", function(){
    document.getElementById("codesModal").classList.remove("open")
});

//Закриття модального вікна при натисканні Esc
window.addEventListener("keydown", (e) => {
    if(e.key == "Escape"){
        document.getElementById("codesModal").classList.remove("open")
    }
});


