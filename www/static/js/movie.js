const params = new URLSearchParams(window.location.search);
const movieId = params.get('id'); // Extract the movie ID
console.log(movieId)

if (movieId) {
    fetchMovieDetails(movieId);
    fetchRelatedMovies(movieId); // Fetch related movies
} else {
    console.error('No movie ID found in the URL.');
}

// Function to fetch movie details
// function fetchMovieDetails(movieId) {
//     const xhr = new XMLHttpRequest();

//     xhr.onreadystatechange = function () {
//         if (xhr.readyState === 4) {
//             if (xhr.status === 200) {
//                 const movie = JSON.parse(xhr.responseText);
//                 displayMovieDetails(movie);
//             } else {
//                 console.error('Failed to fetch movie details:', xhr.status, xhr.statusText);
//                 document.querySelector('.movie-details-container').innerHTML = '<p>Error loading movie details. Please try again later.</p>';
//             }
//         }
//     };

//     xhr.open("GET", `http://127.0.0.1/movies/${movieId}`, true);
//     xhr.send();
// }

// Function to fetch related movies
function fetchRelatedMovies(movieId) {
    const xhr = new XMLHttpRequest();

    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4) {
            if (xhr.status === 200) {
                const allMovies = JSON.parse(xhr.responseText);
                
                // Filter out the current movie ID
                const relatedMovies = allMovies.filter(movie => movie.id !== movieId);
                
                // Display the related movies excluding the current movie
                displayRelatedMovies(relatedMovies);
            } else {
                console.error('Failed to fetch related movies:', xhr.status, xhr.statusText);
            }
        }
    };

    xhr.open("GET", "./movies", true);
    xhr.send();
}

// Function to display the movie details
// function displayMovieDetails(movie) {
//     const movieContainer = document.querySelector('.movie-info'); // Adjusted to target movie-info

//     // Clear the container before adding new movie details
//     movieContainer.innerHTML = '';

//     // Create elements for displaying movie details
//     const imageContainer = document.createElement('div');
//     imageContainer.classList.add('image-container');

//     // Poster
//     const moviePoster = document.createElement('img');
//     moviePoster.src = `https://image.tmdb.org/t/p/w1280${movie.backdrop_path}`;

//     moviePoster.alt = movie.title; // Add alt text for accessibility
//     imageContainer.appendChild(moviePoster);

//     // Overlay for movie details
//     const overlay = document.createElement('div');
//     overlay.classList.add('overlay');

//     // Movie details container
//     const movieDetails = document.createElement('div');
//     movieDetails.classList.add('movie-details');

//     // Title
//     const title = document.createElement('h1');
//     title.textContent = movie.title;
//     movieDetails.appendChild(title);

//     // Info span
//     const infoSpan = document.createElement('div');
//     infoSpan.classList.add('movie-info-span');
    
//     const releaseYear = document.createElement('span');
//     releaseYear.classList.add('info-item');
//     releaseYear.textContent = new Date(movie.release_date).getFullYear(); // Extract year
//     infoSpan.appendChild(releaseYear);

//     const ageRating = document.createElement('span');
//     ageRating.classList.add('info-item', 'age-res');
//     ageRating.textContent = '18+'; // Assuming static for demo
//     infoSpan.appendChild(ageRating);

//     const duration = document.createElement('span');
//     duration.classList.add('info-item');
//     duration.textContent = '120 min'; // Assuming static for demo
//     infoSpan.appendChild(duration);

//     const genres = document.createElement('span');
//     genres.classList.add('info-item');
//     genres.textContent = 'Action, Adventure'; // Assuming static for demo
//     infoSpan.appendChild(genres);

//     movieDetails.appendChild(infoSpan);

//     // Description
//     const description = document.createElement('p');
//     description.textContent = movie.overview || 'No description available.';
//     movieDetails.appendChild(description);

//     // Button container
//     const buttonContainer = document.createElement('div');
//     buttonContainer.classList.add('button-container');

//     const playButton = document.createElement('button');
//     playButton.classList.add('play-button');
//     playButton.innerHTML = '<i class="fa-solid fa-play"></i> Play Movie';
//     buttonContainer.appendChild(playButton);

//     const addToMyListButton = document.createElement('button');
//     addToMyListButton.classList.add('add-to-my-list');
//     addToMyListButton.innerHTML = '<i class="fa-solid fa-plus"></i>';
//     buttonContainer.appendChild(addToMyListButton);

//     const trailerButton = document.createElement('button');
//     trailerButton.classList.add('trailer-btn');
//     trailerButton.innerHTML = '<i class="fa-solid fa-film"></i>';
//     buttonContainer.appendChild(trailerButton);

//     movieDetails.appendChild(buttonContainer);
//     overlay.appendChild(movieDetails);
//     imageContainer.appendChild(overlay);

//     movieContainer.appendChild(imageContainer);
// }

// Function to display related movies
function displayRelatedMovies(relatedMovies) {
    const movieScrollArea = document.getElementById('movie-scroll-area');
    movieScrollArea.innerHTML = ''; // Clear existing movies


    for (let i = 0; i < Math.min(relatedMovies.length, 10); i++) { // Ensure not to exceed the number of available movies
        let movieCard = document.createElement('div');
        movieCard.classList.add('movie_card');
    
         // Set up click event to navigate to landingmovie.html
         movieCard.addEventListener('click', () => {
          window.location.href = `landingmovie.html?id=${relatedMovies[i]['id']}`;
        });
    
        // Poster
        let posterLink = relatedMovies[i]['poster_path'];
        let moviePoster = document.createElement('img');
        moviePoster.src = posterLink;
        moviePoster.alt = relatedMovies[i]['title']; // Add alt text for accessibility
    
        // Overlay for movie details
        let overlay = document.createElement('div');
        overlay.classList.add('overlay');
    
        // Title
        let title = document.createElement('h1'); // Change to h1 for prominence
        title.textContent = relatedMovies[i]['title'];
        overlay.appendChild(title);
    
        // Rating
        let rating = document.createElement('h2');
        rating.textContent = `Rating: ${relatedMovies[i]['vote_average']}`;
        overlay.appendChild(rating);
    
        // Rating stars (assuming you want to display stars)
        let ratingStars = document.createElement('div');
        ratingStars.classList.add('rating');
    
        // Assuming a 5-star rating system
        const starCount = 5;
        const userRating = Math.round(relatedMovies[i]['vote_average'] / 2); // Adjust for 5-star system
    
        for (let j = 1; j <= starCount; j++) {
          const star = document.createElement('i');
          star.className = j <= userRating ? 'fas fa-star' : 'far fa-star'; // Filled or empty star
          ratingStars.appendChild(star);
        }
        ratingStars.appendChild(document.createTextNode(`${userRating}/5`)); // Append rating text
        overlay.appendChild(ratingStars);
    
        // Release Date
        let releaseDate = document.createElement('p');
        releaseDate.textContent = `Release Date: ${new Date(relatedMovies[i]['release_date']).toLocaleDateString()}`;
        overlay.appendChild(releaseDate);
    
        // Description (assuming you have a description field)
        let description = document.createElement('p');
        description.classList.add('desc'); // Add class for styling
    
        // Limit the description length to 100 characters
        const maxLength = 100;
        let overview = relatedMovies[i]['overview'] || 'No description available.';
    
        if (overview.length > maxLength) {
          overview = overview.slice(0, maxLength) + '...'; // Add ellipsis
        }
    
        description.textContent = overview; // Set the limited description
        overlay.appendChild(description);
    
    
        // Append poster and overlay to movie card
        movieCard.appendChild(moviePoster);
        movieCard.appendChild(overlay);
    
        // Append the movie card to the container
        movieScrollArea.appendChild(movieCard);
      }
    
}