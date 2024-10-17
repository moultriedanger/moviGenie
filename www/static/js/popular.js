//ajax teplate taken from https://medium.com/@JavaScript-World/mastering-ajax-in-javascript-a-beginners-guide-with-examples-6111aa53e690
const xhr = new XMLHttpRequest();

xhr.onreadystatechange = function() {
    if (xhr.readyState === 4 && xhr.status === 200) {
      const movies = JSON.parse(xhr.responseText);
      display_movies(movies);
    }
  };
  xhr.open("GET", "http://127.0.0.1:5000/movies", true);
  xhr.send();

function display_movies(movies){

    const movieContainer = document.querySelector('.movie-cards');

    for (let i = 0; i < 10; i++){
        let movieCard = document.createElement('div');
        movieCard.classList.add('movie_card');

        //Poster
        let posterLink = movies[i]['poster_path'];
        let moviePoster = document.createElement('img')
        moviePoster.src = posterLink;

        //Title
        // let title = document.createElement('p')
        // title.textContent = movies[i]['title']
        // movieCard.appendChild(title)

        // // //Rating
        // let popularity= document.createElement('p')
        // popularity.textContent = "Rating: " + movies[i]['vote_average']
        // movieCard.appendChild(popularity)


        movieCard.appendChild(moviePoster)

        movieContainer.appendChild(movieCard);
    }
}