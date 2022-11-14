'use strict';
let numbers = [];
numbers[0] = parseInt(prompt("Please give an integer:"));
numbers[1] = parseInt(prompt("Please give another integer:"));
numbers[2] = parseInt(prompt("Please give a third integer:"));

let sum = 0;
for (var a = 0; a < numbers.length; a++){
    sum  += numbers[a];
    }

let product = 1;
for (var b = 0; b < numbers.length; b++){
    product *= numbers[b];
    }

let average = sum/numbers.length

document.querySelector('#printing').innerHTML = `sum: ${sum} product: ${product} average: ${average}`;