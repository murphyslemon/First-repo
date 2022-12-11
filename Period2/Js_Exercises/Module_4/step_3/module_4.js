'use strict';
// step 3
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

        for (let item of dataFromAPI) {
            const container = document.createElement('show');
            const h2 = document.createElement('h2');
            h2.innerHTML = item['show']['name'];
            container.appendChild(h2);

            const image = document.createElement('img');
            try {
                image.src = item['show']['image']['medium'];
                image.alt = item['show']['name'];
                container.appendChild(image);
                console.log('not null');
            } catch {
                console.log('null');
                image.src = 'https://via.placeholder.com/243x342?text=image';
                image.alt = item['show']['name'];
                container.appendChild(image);
            }

            const genres = document.createElement('ul');
            for (let i = 0; i <= item['show']['genres'].length; i++){
                genres.innerHTML += `<li> ${item['show']['genres'][i]} </li>`
                }
            container.appendChild(genres)

            const description = document.createElement('p');
            description.innerHTML = item['show']['summary'];
            container.appendChild(description);

            const link = document.createElement('a');
            link.href = item['show']['url'];
            link.target = "_blank";
            link.innerHTML = item['show']['url'];
            container.appendChild(link);
            document.body.appendChild(container)
        }

    } catch (error) {
        console.log('error', error);
    }
});

