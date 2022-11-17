'use strict';
let unorderedYearList = []
let startYear = +prompt("What is your starting year?");
let endYear = +prompt("What is your ending year?");
const ul = document.createElement("ul");
for (let i = startYear; i <= endYear; i++){
    if ((i % 4 === 0) && (i % 100 !== 0) || (i % 400 === 0)) {
      ul.innerHTML += `<li> ${i} </li>`
    }
}

console.log(unorderedYearList);

document.body.appendChild(ul)