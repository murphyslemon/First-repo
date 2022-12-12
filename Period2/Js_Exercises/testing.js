async function getTVMazeInfo(keyword) {
    let json_response;
    try {
        const response  = await fetch("https://api.tvmaze.com/search/shows?q=" + keyword);
        json_response   = await response.json();
    }
    catch (error) {
        console.log(error.message);
    }

    return json_response;
}



document.getElementById("search-button").addEventListener("click", async (e) => {
    e.preventDefault();

    const checkContainer = document.getElementById("container");
    if (checkContainer !== null) {
        checkContainer.remove();
    }

    const keyword = document.getElementById("search-box").value;
    //console.log(keyword);
    const apiResult = await getTVMazeInfo(keyword);
    //console.log(apiResult);


    const container = document.createElement("div");
    container.id = "container";

    for (let i = 0; i < apiResult.length; i++) {
        const art   = document.createElement("article");
        const name  = document.createElement("h3");
        const genre = document.createElement("p");

        art.classList.add("card");
        genre.classList.add("genre");
        genre.innerText = "Genres: ";

        if (apiResult[i].show.genres.length === 0) {
            genre.innerText += "Unknown";
        }
        else if (apiResult[i].show.genres.length === 1) {
            genre.innerText += apiResult[i].show.genres;
        }
        else {
            genre.innerText += apiResult[i].show.genres[0];
            for (let j = 1; j < apiResult[i].show.genres.length; j++) {
                genre.innerText += ` | ${apiResult[i].show.genres[j]}`;
            }
        }

        const link      = document.createElement("a");
        const img_med   = document.createElement("img");
        const summary   = document.createElement("div");

        summary.classList.add("summary");

        name.innerText  = apiResult[i].show.name;

        link.target     = "_blank";
        link.innerText  = "Link to TV Maze";
        link.href       = apiResult[i].show.url;


        if (apiResult[i].show.image === null) {
            img_med.src = "https://via.placeholder.com/100x200?text=No+image";
        }
        else {
            img_med.src = apiResult[i].show.image.medium;
        }

        img_med.alt     = "image";
        summary.innerHTML = apiResult[i].show.summary;

        art.appendChild(img_med);
        art.appendChild(name);
        art.appendChild(genre);
        art.appendChild(link);
        art.appendChild(summary);

        container.appendChild(art);
    }

    document.body.appendChild(container);




})