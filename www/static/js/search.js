const API_KEY = 'https://api.themoviedb.org/3/discover/movie?&sort_by=popularity.desc?&api_key=e62d70da841d21d5d75dd74e2b9d6cbf&query=&page=1'
const IMG_PATH = 'https://image.tmdb.org/t/p/w1280'
const SEARCHAPI = "https://api.themoviedb.org/3/search/movie?&api_key=e62d70da841d21d5d75dd74e2b9d6cbf&query=";

search_box = document.getElementById('search-input');

search_box.addEventListener('change', async function() {

    var search_param = search_box.value
    search_box.value = '';
    
    console.log(search_param)
    var data_link = SEARCHAPI + search_param

    try {
        const response = await fetch(data_link);
        const data = await response.json();
        // console.log(data);
        createPopup(data)
    } catch (error) {
        console.error("Error fetching data:", error);
    }
});

function createPopup(data) {
    
    // Create the overlay
    const overlay = document.createElement('div');
    overlay.className = 'search_overlay';

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
    overlay.appendChild(closeButton);

    // Append the popup to the overlay
    // overlay.appendChild(popup);
    document.body.appendChild(overlay);

    //Get movies. Show top 5 results
    let movies = data['results']
    console.log(movies)

    // let movie_container = document.createElement('div')
    // movie_container.classList.add('movie_list');

    for (let i = 0; i < 5; i++) {
        
        let movieCard = document.createElement('div');
        movieCard.classList.add('movie_card');

        //Get poster id and add onclidk to the movieCard
        let posterId = movies[i]['id']
        
        let link = document.createElement('a');
        link.href = `/trending_movie/${posterId}`;
        
        // Poster
        let poster_base = "https://image.tmdb.org/t/p/w1280"
        let posterLink = movies[i]['poster_path']
        let full = poster_base + posterLink

        let moviePoster = document.createElement('img');
        moviePoster.src = full;
        moviePoster.alt = movies[i]['title']; // Add alt text for accessibility

         // Append poster and overlay to movie card
        movieCard.appendChild(moviePoster);

        link.appendChild(movieCard)

        // movie_container.appendChild(link)
        overlay.appendChild(link)

        // overlay.appendChild(movie_container)      
    }
}