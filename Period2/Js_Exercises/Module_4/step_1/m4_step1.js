'use strict';
// step 1
document.addEventListener('submit', async function(evt) {
    evt.preventDefault();
    const inputValue = document.querySelector('#query').value
    try {
        const proxy = 'https://api.allorigins.win/get?url=';
        const search = 'https://api.tvmaze.com/search/shows?q='+ inputValue;
        const url = proxy + encodeURIComponent(search);

        const response = await fetch(url);
        if (!response.ok) throw new Error('Invalid input!');
        const result = await response.json();
        const dataFromAPI = JSON.parse(result.contents);
        console.log(dataFromAPI)
    } catch (e) {
        console.log('error', e);
    }
});

