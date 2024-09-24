async function get_json(){

    let response = await fetch('data.json');
    console.log('no error');

    let movies = await response.json();

    for (movie of movies){
        let movie_card = document.createElement("div");
    movie_card.className = "movie-card";

    //title
    let title = document.createElement('h1')
    title.textContent = movie.original_title
    movie_card.appendChild(title)

    //poster
    let poster = document.createElement('img')
    // popularity.textContent = "Rating: " + movie.vote_average
    movie_card.appendChild(poster)

    // img.src = 'https://example.com/image.jpg'; 
    // img.alt = 'An example image';              
    // img.width = 100;                           
    // mg.height = 100; 

    //description
    let release_date = document.createElement('h2')
    release_date.textContent = "Release date: " + movie.release_date
    movie_card.appendChild(release_date)

    //Rating
    let popularity= document.createElement('h2')
    popularity.textContent = "Rating: " + movie.vote_average
    movie_card.appendChild(popularity)
    
    let movie_div = document.getElementById("movie-collection");

    movie_div.appendChild(movie_card);

    }

}
get_json();