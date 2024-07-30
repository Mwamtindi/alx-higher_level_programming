#!/usr/bin/node

const request = require('request');

// Get the API URL from the command line arguments
const aapiUrl = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}/`;

request(aapiUrl, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const charactersUrls = JSON.parse(body).characters;

    const fetchCharacterName = (characterUrl) => {
      request(characterUrl, function (error, response, body) {
        if (!error && response.statusCode === 200) {
          const characterData = JSON.parse(body);
          console.log(characterData.name);
        } else {
          console.error(`Error: Failed to retrieve the character data. Status code: ${response.statusCode}`);
        }
      });
    };

    charactersUrls.forEach(fetchCharacterName);
  } else {
    console.error(`Error: Failed to retrieve the movie data. Status code: ${response.statusCode}`);
  }
});
