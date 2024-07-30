#!/usr/bin/node

const request = require('request');

// Get the URL and file path from the command line arguments
const apiUrl = process.argv[2];

const characterId = 18;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const filmsData = JSON.parse(body).results;
    const moviesWithWedge = filmsData.filter((film) =>
      film.characters.includes(
        `https://swapi-api.alx-tools.com/api/people/${characterId}/`
      )
    );
    console.log(moviesWithWedge.length);
  }
});
