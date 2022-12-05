const button = document.querySelector('#start');
const p = document.querySelector('#result');
const select = document.querySelector("#operation");



button.addEventListener('click', operations);

function operations() {
    let num1 = +(document.querySelector('#num1').value);
    let num2 = +(document.querySelector('#num2').value);
 

    if (select.value === 'add'){
        let result = num1 + num2;
        p.innerHTML = `Answer: ${result}`;
    }
    if (select.value ==='sub'){
        let result = num1 - num2;
        p.innerHTML = `Answer: ${result}`;
    }
    if (select.value === 'multi'){
        let result = num1 * num2;
        p.innerHTML = `Answer: ${result}`;
    }
    if (select.value === 'div'){
        let result = num1 / num2;
        p.innerHTML = `Answer: ${result}`;
    } 
}