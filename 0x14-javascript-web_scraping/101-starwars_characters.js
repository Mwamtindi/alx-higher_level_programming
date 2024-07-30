#!/usr/bin/node

const request = require('request');

// Get the API URL from the command line arguments
const apiUrl = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request(apiUrl, function (error, response, body) {
  if (!error) {
    const characters = JSON.parse(body).characters;

    printCharacters(characters, 0);
  }
});

// A function to print characters recursively
function printCharacters (characters, idx) {
  request(characters[idx], function (error, response, body) {
    if (!error) {
      console.log(JSON.parse(body).name);

      if (idx + 1 < characters.length) {
        printCharacters(characters, idx + 1);
      }
    }
  });
}
