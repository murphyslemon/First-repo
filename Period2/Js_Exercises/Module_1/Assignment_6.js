'use strict';
let answer = confirm("Should I calculate the square root?");
if (answer === true) {
    let number = prompt("What number do you want to square root?");
    if (number < 0) {
        document.querySelector('#printing').innerHTML = `The square root of a negative number is not defined.`;
    } else {
        let squareRoot = Math.sqrt(number);
        document.querySelector('#printing').innerHTML = `The square root of ${number} is ${squareRoot}.`;
    }
}
if (answer === false) {
    document.querySelector('#printing').innerHTML = `The square root is not calculated.`;
}