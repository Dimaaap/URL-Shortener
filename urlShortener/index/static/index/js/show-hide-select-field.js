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

const urlshortener = document.getElementById("default-choice");

urlshortener.onclick = () => {
    const form = document.getElementById('input-url-form');
    let inputDomainField = document.getElementById('domain-input-field')
    let textToInsert = "shortenurl.com"
    inputDomainField.value = textToInsert;
}


document.getElementById("input-url-form").addEventListener("submit", function(event){
    event.preventDefault();
    let formData = new FormData(this);
    axios.post(window.location.href, formData)
        .then(function(response){
            let newFormHtml = response.data.new_form_html;
            //var newFormContainer = document.getElementById("newFormContainer");
            var oldFormContainer = document.getElementById('main-form');
            oldFormContainer.innerHTML = newFormHtml;
            isShortenForm = true;
            //newFormContainer.innerHTML =newFormHtml
        })
        .catch(function(error){
            console.log(error);
        });
});


function openQRModal(){
        var modal = document.getElementById("modal");
        console.log(modal)
        modal.style.display = "block";
        console.log("Open a modal window");
}

window.addEventListener('click', function(event){
    if(event.target === modal) {
        modal.style.display = 'none';
    }
});

function generateQRCode(){
    var qrcode = new QRCode("qrcode");
    var data = document.getElementById("id_user_url").value;
    qrcode.makeCode(data);
    console.log(qrcode);
}
