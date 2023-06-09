

document.querySelector('.card-number-input').oninput = () =>{
    document.querySelector('.card-no').textContent  = document.querySelector('.card-number-input').value;
}


document.querySelector('.card-holder-input').oninput = () =>{
    document.getElementById('.card-holder-name').textContent = document.querySelector('.card-holder-input').value;
}

document.querySelector('.month-input').oninput = () =>{
    document.getElementById('.exp-month').innerText = document.querySelector('.month-input').value;
}

document.querySelector('.year-input').oninput = () =>{
    document.getElementById('.exp-year').innerText = document.querySelector('.year-input').value;
}

document.querySelector('.cvv-input').oninput = () =>{
    document.querySelector('.cvv-box').innerText = document.querySelector('.cvv-input').value;
}
