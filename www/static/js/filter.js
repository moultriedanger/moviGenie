function applyFilters() {
    const genre = document.getElementById('genre').value;
    const startDate = document.getElementById('start-date').value;
    const endDate = document.getElementById('end-date').value;
    const minRating = document.getElementById('min-rating').value;

    // Build query string
    const params = new URLSearchParams({
        genre: genre || undefined,
        start_date: startDate || undefined,
        end_date: endDate || undefined,
        min_rating: minRating || undefined,
    });

    // Fetch filtered movies
    fetch('/moviGenie/movies?${params.toString()}')
        .then(response => response.json())
        .then(data => {
            displayMovies(data); // Function to update the UI with filtered movies
        })
        .catch(error => console.error('Error fetching movies:', error));
}

function displayMovies(movies) {
    const movieContainer = document.getElementById('movie-list'); // Replace with your container
    movieContainer.innerHTML = '';

    movies.forEach(movie => {
        const movieCard = `
            <div class="movie_card" onclick="window.location.href='moviGenie/trending_movie/${movie.id}'">
                <img src="https://image.tmdb.org/t/p/w1280${movie.poster_path}" alt="Movie Poster" />
                <h1>${movie.title}</h1>
                <p>Rating: ${movie.vote_average}</p>
                <p>Release Date: ${movie.release_date}</p>
            </div>
        `;
        movieContainer.innerHTML += movieCard;
    });
}
