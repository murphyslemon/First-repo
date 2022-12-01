const ul = document.querySelector('#target');
let items = ["First item", "Second item", "third item"]

for (let i = 0; i < items.length; i++) {
    const li = document.createElement('li');
    li.innerHTML = items[i];
    ul.appendChild(li);
}

const second_item = document.querySelectorAll('li')[1];
second_item.classList.add("my-item");