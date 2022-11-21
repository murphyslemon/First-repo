'use strict';
let number_participants = +prompt("How many participants are there?");
let participants = [];

for (let a = 0; a < number_participants; a++){
    participants.push(prompt("Please give a participant's name"));
    }

participants.sort();
const ol = document.createElement('ol');

for (let i = 0; i < participants.length; i++){
    ol.innerHTML += `<li> ${participants[i]} </li>`;
    }

document.body.appendChild(ol);

