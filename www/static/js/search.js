const API_KEY = 'https://api.themoviedb.org/3/discover/movie?&sort_by=popularity.desc?&api_key=e62d70da841d21d5d75dd74e2b9d6cbf&query=&page=1'
const IMG_PATH = 'https://image.tmdb.org/t/p/w1280'
const SEARCHAPI = "https://api.themoviedb.org/3/search/movie?&api_key=e62d70da841d21d5d75dd74e2b9d6cbf&query=";

search_box = document.getElementById('search-input');

search_box.addEventListener('change', async function() {

    var search_param = search_box.value
    console.log(search_param)
    var data_link = SEARCHAPI + search_param

    try {
        const response = await fetch(data_link);
        const data = await response.json();
        console.log(data);

        createPopup(data)
    } catch (error) {
        console.error("Error fetching data:", error);
    }

});

function createPopup(data) {
    
    // Create the overlay
    const overlay = document.createElement('div');
    overlay.className = 'overlay'; // Add overlay class

    // Create the square popup container
    const popup = document.createElement('div');
    popup.className = 'popup'; // Add popup class

    // Create the close button
    const closeButton = document.createElement('button');
    closeButton.textContent = 'Close'; // Button text
    closeButton.className = 'close-button'; // Add a class for styling

    // Add an event listener to the close button
    closeButton.addEventListener('click', function() {
        document.body.removeChild(overlay); // Remove overlay (and popup) when clicked
    });

    // Append the close button to the popup
    popup.appendChild(closeButton);

    // Append the popup to the overlay
    overlay.appendChild(popup);
    document.body.appendChild(overlay);

    
    // for(movie of movies){
    //     // console.log(movie)

    //     const popup = document.createElement('div');
    //     popup.classList.add('popup');

    //     // const title = document.createElement('h2');
    //     // title.textContent = movie.title;
    //     // popup.appendChild(title)
}


    //     // let posterLink = movies[i]['poster_path'];
    //     // let moviePoster = document.createElement('img');
    //     // moviePoster.src = posterLink;
    //     // moviePoster.alt = movies[i]['title']; // Add alt text for accessibility


        
    // }

    // for (let i = 0; i < Math.min(movies.length, 3); i++) {
    //     let movieCard = document.createElement('div');
    //     movieCard.classList.add('movie_card');
    

    // }

    // // Populate the popup with data (you can modify this based on your data structure)
    // const title = document.createElement('h2');
    // title.textContent = "Search Results";
    // popup.appendChild(title);

    // const content = document.createElement('p');
    // content.textContent = JSON.stringify(data, null, 2); // Display the data in a readable format
    // popup.appendChild(content);

    // // Create a close button
    // const closeButton = document.createElement('button');
    // closeButton.textContent = "Close";
    // closeButton.addEventListener('click', function() {
    //     overlay.remove(); // Remove the popup when clicked
    // });
    // popup.appendChild(closeButton);

    // // Append the popup to the body inside the overlay
    // overlay.appendChild(popup);
    // document.body.appendChild(overlay);
