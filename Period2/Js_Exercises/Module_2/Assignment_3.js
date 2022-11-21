'use strict';
let dogs = [];
for (let a = 0; a < 6; a++){
    dogs.push(prompt("Please give a dog's name"));
    }

dogs.sort();
dogs.reverse();

const ul = document.createElement('li');

for (let i = 0; i < dogs.length; i++){
    ul.innerHTML += `<li> ${dogs[i]} </li>`;
    }

document.body.appendChild(ul);