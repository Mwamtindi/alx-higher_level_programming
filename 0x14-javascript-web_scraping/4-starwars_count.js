#!/usr/bin/node

const request = require('request');

// Get the URL and file path from the command line arguments
const apiUrl = process.argv[2];

if (!apiUrl) {
  console.error('Error: The API URL not provided.');
  process.exit(1);
}

const characterId = 18;

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    if (response.statusCode === 200) {
      const filmsData = JSON.parse(body);
      const moviesWithCharacter = filmsData.results.filter((film) =>
        film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)
      );
      console.log(moviesWithCharacter.length);
    } else {
      console.error(`Error: Failed to retrieve the movies data. Status code: ${response.statusCode}`);
    }
  }
});
