'use strict';
let rolls = [];
let numberOfDice = parseInt(prompt("How many dice do you want to roll?"));

for (var a = 0; a < numberOfDice; a++) {
    let roll = Math.floor(Math.random() * 6) + 1;
    rolls.push(roll);
}

for (let i = 0; i < rolls.length; i++){
  console.log(rolls[i]);
  document.querySelector('#printing').innerHTML = `${rolls[i]}\n`;
}

let sum = 0;
for (var b = 0; b < rolls.length; b++){
    sum  += rolls[b];
    }
document.querySelector('#printing').innerHTML = `The total sum of you ${numberOfDice} dice is equal to ${sum}.`;