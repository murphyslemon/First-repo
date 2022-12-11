'use strict';
// step 2
document.addEventListener('submit', async function(evt) {
    evt.preventDefault();
    const inputValue = document.querySelector('#query').value;
    try {
        const proxy = 'https://api.allorigins.win/get?url=';
        const search = 'https://api.tvmaze.com/search/shows?q='+ inputValue;
        const url = proxy + encodeURIComponent(search);

        const response = await fetch(url);
        if (!response.ok) throw new Error('Invalid input!');
        const result = await response.json();
        const dataFromAPI = JSON.parse(result.contents);

        const container = document.getElementById('show');
        const h2 = document.createElement('h2');
        h2.innerHTML = dataFromAPI[0]['show']['name'];
        container.appendChild(h2);

        const image = document.createElement('img');
        image.src = dataFromAPI[0]['show']['image']['medium'];
        image.alt = dataFromAPI[0]['show']['name'];
        container.appendChild(image);

        const description = document.createElement('p');
        description.innerHTML = dataFromAPI[0]['show']['summary'];
        container.appendChild(description);

        const link = document.createElement('a');
        link.href = dataFromAPI[0]['show']['url'];
        link.target = "_blank";
        link.innerHTML = dataFromAPI[0]['show']['url'];
        container.appendChild(link);

    } catch (error) {
        console.log('error', error);
    }
});

