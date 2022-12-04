'use strict';
const names = ['John', 'Paul', 'Jones'];
const ul = document.querySelector('#target');

//testing another way
// names.forEach(function (item,index) {
//     const li = document.createElement('li');
//     li.innerHTML=names[index];
//     ul.appendChild(li);
// })

for (let i=0; i<names.length; i++) {
    const li = document.createElement('li');
    li.innerHTML=names[i];
    ul.appendChild(li);
}

