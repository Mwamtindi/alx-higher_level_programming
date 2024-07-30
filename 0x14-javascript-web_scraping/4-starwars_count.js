#!/usr/bin/node

const request = require('request');

// Get API URL from the command line arguments
const apiUrl = process.argv[2];

if (!apiUrl) {
  console.error('Usage: ./4-wedgecount.js <api_url>');
  process.exit(1);
}

// A function to check if Wedge Antilles is in the movie
const isWedgeInMovie = (film, callback) => {
  request.get(film, (error, response, body) => {
    if (error) {
      console.error('Error:', error);
      return callback(error);
    }

    const data = JSON.parse(body);
    if (data.characters && data.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')) {
      callback(null, true);
    } else {
      callback(null, false);
    }
  });
};

// Fetch list of films
request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    process.exit(1);
  }

  const data = JSON.parse(body);
  if (!data.results || !Array.isArray(data.results)) {
    console.error('Invalid data format');
    process.exit(1);
  }

  let count = 0;
  let pendingRequests = data.results.length;

  data.results.forEach(film => {
    isWedgeInMovie(film.characters[0], (err, isInMovie) => {
      if (err) {
        console.error('Error:', err);
      } else if (isInMovie) {
        count++;
      }

      pendingRequests--;

      if (pendingRequests === 0) {
        console.log(count);
      }
    });
  });
});
