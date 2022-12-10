'use strict';
// step 1
document.addEventListener('submit', async function(evt) {
    evt.preventDefault();
    const inputValue = document.querySelector('#query').value
    try {
        const proxy = 'https://api.allorigins.win/get?url=';
        const search = 'https://api.tvmaze.com/search/shows?q='+ inputValue;
        console.log(search)
        const url = proxy + encodeURIComponent(search);
        console.log(url)
        const response = await fetch(url);
        if (!response.ok) throw new Error('Invalid input!');
        const json = await response.json();
        console.log('result', json.contents);
    } catch (e) {
        console.log('error', e);
    }
});

// step 2
