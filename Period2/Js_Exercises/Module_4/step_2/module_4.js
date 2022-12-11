'use strict';
// step 2
document.addEventListener('submit', async function(evt) {
    evt.preventDefault();
    const inputValue = document.querySelector('#query').value;
    try {
        const search = 'https://api.tvmaze.com/search/shows?q='+ inputValue;
        const response = await fetch(search);
        const json = await response.json();

        const container = document.getElementById('show');
        const h2 = document.createElement('h2');
        h2.innerHTML = json[0]['show']['name'];
        container.appendChild(h2);

        const image = document.createElement('img');
        image.src = json[0]['show']['image']['medium'];
        image.alt = json[0]['show']['name'];
        container.appendChild(image);

        const description = document.createElement('p');
        description.innerHTML = json[0]['show']['summary'];
        container.appendChild(description);

        const url = document.createElement('a');
        url.href = json[0]['show']['url'];
        url.target = "_blank";
        url.innerHTML = json[0]['show']['url'];
        container.appendChild(url);

    } catch (e) {
        console.log('error', e);
    }
});

