'use strict';
const names = ['John', 'Paul', 'Jones'];
const ul = document.querySelector('#target');

names.forEach(function (item,index) {
    const li = document.createElement('li');
    li.innerHTML=names[index];
    ul.appendChild(li);
})

