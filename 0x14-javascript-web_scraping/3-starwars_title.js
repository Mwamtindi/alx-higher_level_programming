#!/usr/bin/node

const request = require('request');

// Get movie ID from the command line arguments
const movieId = process.argv[2];

if (!movieId) {
  console.error('Usage: ./3-swtitle.js <movie_id>');
  process.exit(1);
}

// Construct API URL
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

// Perform GET request to Star Wars API
request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  // Parse JSON response
  const data = JSON.parse(body);

  // Check if response contains title
  if (data.title) {
    console.log(data.title);
  } else {
    console.error('Movie not found or invalid ID.');
  }
});
