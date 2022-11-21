'use strict';
let numbers = [];
numbers[4] = +prompt("What is your first number?");
numbers[3] = +prompt("What is your second number?");
numbers[2] = +prompt("What is your third number?");
numbers[1] = +prompt("What is your fourth number?");
numbers[0] = +prompt("What is your fifth number?");

for (let a = 0; a < numbers.length; a++){
    console.log(numbers[a]);
    }