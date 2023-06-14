const domainField = document.getElementById("domain-input-field");
toggleBtn = document.getElementById("select-arrow")

let popup = document.getElementById("select-popup");

toggleBtn.onclick = ()=>{
     if(popup.style.display == "none"){
        popup.style.display = 'block';
        toggleBtn.src = "   https://cdn-icons-png.flaticon.com/512/3838/3838683.png ";
     } else {
        popup.style.display = 'none';
        toggleBtn.src = "   https://cdn-icons-png.flaticon.com/512/2985/2985150.png ";
     }
}