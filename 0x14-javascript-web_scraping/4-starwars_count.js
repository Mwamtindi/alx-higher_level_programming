#!/usr/bin/node

const request = require('request');
let numb = 0;

// Get the URL and file path from the command line arguments
request.get(process.argv[2], (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const content = JSON.parse(body);
    content.results.forEach((film) => {
      film.characters.forEach((character) => {
        if (character.includes(18)) {
          numb += 1;
        }
      });
    });
    console.log(numb);
  }
});
