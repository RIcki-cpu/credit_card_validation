$(window).on("load",function(){
 $(".loader-wrapper").fadeOut("slow");
});
    
 document.querySelector('.card-number-input').oninput = () =>{
const textinput = document.querySelector('.card-number-input').value;
const result = textinput.match(/.{1,4}/g).join(" ");
    
document.querySelector('.card-no').textContent  = result
}
    
    
document.querySelector('.card-holder-input').oninput = () =>{
    // window.alert(document.getElementById('card-holder-name').innerText);
document.querySelector('.card-holder-name').textContent = document.querySelector('.card-holder-input').value;
 }
    
 document.querySelector('.month-input').oninput = () =>{
document.querySelector('.exp-month').textContent = document.querySelector('.month-input').value;
}
    
document.querySelector('.year-input').oninput = () =>{
 document.querySelector('.exp-year').textContent = document.querySelector('.year-input').value;
}
    
 document.querySelector('.cvv-input').oninput = () =>{
document.querySelector('.cvv-box').textContent  = document.querySelector('.cvv-input').value;
}
const form = document.getElementById('form');
form.addEventListener('submit',function(e){
e.preventDefault();
showLoader(); 

// Get the form inputs
var cardNumber = document.querySelector('.card-number-input').value;
//var cardHolder = document.querySelector('.card-holder-input').value;
var expirationMonth = document.querySelector('.month-input').value;
var expirationYear = document.querySelector('.year-input').value-2000;
var cvv = document.querySelector('.cvv-input').value;

const expirationDate = expirationMonth + "/" + expirationYear 

// Construct the request body
var requestBody = {
card_number: cardNumber,
expiration_date: expirationDate,
cvv: cvv
};

console.log(requestBody);

// Send the POST request
fetch('https://apicard-1-v6371899.deta.app/validate_credit_card', {
method: 'POST',
headers: {
'Content-Type': 'application/json'
},
body: JSON.stringify(requestBody)
}).then(response => response.json()
)
.then(data => {
console.log('Success:', data);
hideLoader();
showPopupMessage(data.valid, data.message);
})
.catch(function(error) {
hideLoader();
// Handle any errors that occurred during the request
alert('An error occurred: ' + error.message);

}); 

})

function showLoader() {
$(".loader-wrapper").fadeIn("slow");
}

function hideLoader() {
//document.querySelector('.loader-wrapper').style.display = 'none';
$(".loader-wrapper").fadeOut("slow");
}




function showPopupMessage(valid, message) {
const popup = document.createElement('div');
popup.className = valid ? 'success-popup' : 'failure-popup';
popup.innerHTML = `
<i class="${valid ? 'fas fa-check-circle' : 'fas fa-times-circle'}"></i>
<span>${message}</span>
`;

const popupContainer = document.getElementById('popup');
popupContainer.innerHTML = '';
popupContainer.appendChild(popup);
}

//new object FormData Array[Array[2]]
/*const payload = new FormData(form)
console.log([...payload]);*/