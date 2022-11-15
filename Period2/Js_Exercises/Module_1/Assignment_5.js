'use strict';
let year = prompt("What year do you want to check?");
if (year % 4 === 0) {
    if (year % 100 === 0) {
        if (year % 400 === 0) {
            document.querySelector('#printing').innerHTML = `${year} is a leap year.`;
        } else {
            document.querySelector('#printing').innerHTML = `${year} is not leap year.`;
        }
    } else {
        document.querySelector('#printing').innerHTML = `${year} is a leap year.`;
    }
} else {
    document.querySelector('#printing').innerHTML = `${year} is not a leap year.`;
}