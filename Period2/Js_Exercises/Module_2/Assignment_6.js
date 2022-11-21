'use strict';
let rolls = [];
const ul = document.createElement('ul');

function rollDice() {
    return Math.floor(Math.random() * 6) +1;
}

while (rolls.includes(6) !== true) {
    let x = rollDice();
    rolls.push(x);
    ul.innerHTML += `<li> ${x} </li>`
}

document.body.appendChild(ul);