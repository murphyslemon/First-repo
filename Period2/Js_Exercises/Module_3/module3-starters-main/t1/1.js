let ul = document.querySelector('#target');
ul.innerHTML += "additional HTML code"
const li =
            `<li>First item</li>
            <li>Second item</li>
            <li>Third item</li>`;
ul.innerHTML = li;
ul.classList.add("myList");