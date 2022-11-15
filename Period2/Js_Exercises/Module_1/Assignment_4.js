'use strict';
let studentName = prompt("What is your name?");
let house = Math.floor(Math.random()*4);
console.log(house)

if (house === 0) {
    document.querySelector('#printing').innerHTML = `${studentName}, you are in Griffindor.`;
}

if (house === 1) {
    document.querySelector('#printing').innerHTML = `${studentName}, you are in Slytherin.`;
}

if (house === 2) {
    document.querySelector('#printing').innerHTML = `${studentName}, you are in Huffelpuff.`;
}

if (house === 3) {
    document.querySelector('#printing').innerHTML = `${studentName}, you are in Ravenclaw.`;
}
