// Approach
// Basic Sentiment Analysis: Implement a function to classify words as positive, negative, or neutral.
// Genre and Keyword Matching: Match keywords like “happy” with genres (e.g., comedy) or descriptions that are generally associated with positive feelings.
// Return Matching Movies: Filter movies based on matched genres, keywords, or themes. 
 
 
 
 
 
 
 // Basic keywords for sentiment-based matching
 const moodKeywords = {
    happy: ["happy", "joy", "uplifting", "comedy", "feel-good"],
    sad: ["sad", "down", "emotional", "drama"],
    action: ["exciting", "action", "thrill", "intense"],
    sciFi: ["science fiction", "sci-fi", "future", "space"]
  };

  // Function to determine mood based on input
  function determineMood(input) {
    const lowerInput = input.toLowerCase();

    for (let mood in moodKeywords) {
      if (moodKeywords[mood].some(keyword => lowerInput.includes(keyword))) {
        return mood; // Return matched mood
      }
    }
    return null;
  }

  // Function to get recommendations based on mood
  function getRecommendation(input) {
    const mood = determineMood(input);
    if (!mood) return [];

    // Filter movies based on the mood or genre keywords
    return movies.filter(movie => {
      if (mood === "happy" && movie.genre_ids.includes(35)) return true; // Comedy
      if (mood === "sad" && movie.genre_ids.includes(18)) return true; // Drama
      if (mood === "action" && movie.genre_ids.includes(28)) return true; // Action
      if (mood === "sciFi" && movie.genre_ids.includes(878)) return true; // Sci-Fi
      return movie.overview.toLowerCase().includes(mood);
    }).slice(0, 3); // Limit to top 3 results
  }

  // Event listener for button click
  document.getElementById('recommendButton').addEventListener('click', () => {
    const input = document.getElementById('gptInput').value;
    const recommendedMovies = getRecommendation(input);

    // Display recommendations
    const recommendationDiv = document.getElementById('recommendation');
    recommendationDiv.innerHTML = recommendedMovies.map(movie => `
      <div style="margin-bottom: 20px;">
        <img src="${movie.poster_path}" alt="${movie.title}" width="100">
        <h3>${movie.title} (${new Date(movie.release_date).getFullYear()})</h3>
        <p>Rating: ${movie.vote_average} / 10 (${movie.vote_count} votes)</p>
        <p>${movie.overview}</p>
      </div>
    `).join('') || '<p>No recommendations found.</p>';
  });