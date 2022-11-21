'use strict';
let numbers = [];
let x = +prompt("Please enter a number");
while (x !== 0) {
    numbers.push(x);
    x = +prompt("Please enter a number");
}

numbers.sort();
numbers.reverse();

for (let i = 0; i < numbers.length; i++){
    console.log(numbers[i])
    }