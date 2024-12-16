//ajax teplate taken from https://medium.com/@JavaScript-World/mastering-ajax-in-javascript-a-beginners-guide-with-examples-6111aa53e690
const xhr = new XMLHttpRequest();

xhr.onreadystatechange = function () {
  if (xhr.readyState === 4 && xhr.status === 200) {
    const movies = JSON.parse(xhr.responseText);
    display_movies(movies);
  }
};
xhr.open("GET", "moviGenie/movies", true);
xhr.send();

function display_movies(movies) {

  const movieContainer = document.querySelector('.trending-cards');

  // Clear the container before adding new movies
  movieContainer.innerHTML = '';

  for (let i = 0; i < Math.min(movies.length, 10); i++) { // Ensure not to exceed the number of available movies
    let movieCard = document.createElement('div');
    movieCard.classList.add('movie_card');

    //Get poster id and add onclidk to the movieCard
    let posterId = movies[i]['id']
    
    let link = document.createElement('a');
    link.href = `/trending_movie/${posterId}`;
    
    // Poster
    let posterLink = movies[i]['poster_path'];
    let moviePoster = document.createElement('img');
    moviePoster.src = posterLink;
    moviePoster.alt = movies[i]['title']; // Add alt text for accessibility

    // Overlay for movie details
    let overlay = document.createElement('div');
    overlay.classList.add('overlay');

    // Title
    let title = document.createElement('h1'); // Change to h1 for prominence
    title.textContent = movies[i]['title'];
    overlay.appendChild(title);

    // Rating
    let rating = document.createElement('h2');
    rating.textContent = `Rating: ${movies[i]['vote_average']}`;
    overlay.appendChild(rating);

    // Rating stars (assuming you want to display stars)
    let ratingStars = document.createElement('div');
    ratingStars.classList.add('rating');

    // Assuming a 5-star rating system
    const starCount = 5;
    const userRating = Math.round(movies[i]['vote_average'] / 2); // Adjust for 5-star system

    for (let j = 1; j <= starCount; j++) {
      const star = document.createElement('i');
      star.className = j <= userRating ? 'fas fa-star' : 'far fa-star'; // Filled or empty star
      ratingStars.appendChild(star);
    }
    ratingStars.appendChild(document.createTextNode(`${userRating}/5`)); // Append rating text
    overlay.appendChild(ratingStars);

    // Release Date
    let releaseDate = document.createElement('p');
    releaseDate.textContent = `Release Date: ${new Date(movies[i]['release_date']).toLocaleDateString()}`;
    overlay.appendChild(releaseDate);

    // Description (assuming you have a description field)
    let description = document.createElement('p');
    description.classList.add('desc'); // Add class for styling
   
    // Limit the description length to 100 characters
    const maxLength = 100;
    let overview = movies[i]['overview'] || 'No description available.';

    if (overview.length > maxLength) {
      overview = overview.slice(0, maxLength) + '...'; // Add ellipsis
    }

    description.textContent = overview; // Set the limited description
    overlay.appendChild(description);

    // Append poster and overlay to movie card
    movieCard.appendChild(moviePoster);
    movieCard.appendChild(overlay);

    link.appendChild(movieCard);

    // Append the movie card to the container
    movieContainer.appendChild(link);
  }
}

