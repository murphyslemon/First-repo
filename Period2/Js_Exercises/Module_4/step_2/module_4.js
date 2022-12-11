'use strict';
// step 2
document.addEventListener('submit', async function(evt) {
    evt.preventDefault();
    const inputValue = document.querySelector('#query').value
    try {
        const search = 'https://api.tvmaze.com/search/shows?q='+ inputValue;
        const response = await fetch(search);
        const json = await response.json();
        console.log(json);
        for (const item of json) {
            console.log(item['show']['name'])
            console.log(item['show']['url'])
            console.log(item['show']['image']['medium'])
            console.log(item['show']['summary'])
        }
    } catch (e) {
        console.log('error', e);
    }
});

