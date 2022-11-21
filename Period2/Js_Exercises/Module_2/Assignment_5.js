'use strict';
let numbers = [];
let x = +prompt("Please enter a number");

while (numbers.includes(x) !== true) {
    let x = +prompt("Please enter a number");
    numbers.push(x);
}
for (let i = 0; i < numbers.length; i++) {
    console.log(numbers[i]);
}
alert("That number has already been used.");

