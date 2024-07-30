#!/usr/bin/node

const request = require('request');
const fs = require('fs');

// Get the URL and file path from the command line arguments
const url = process.argv[2];
const filePath = process.argv[3];

if (!url || !filePath) {
  console.error('Error: Both URL and file path must be provided.');
  process.exit(1);
}

// Perform a GET request to the URL
request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    fs.writeFile(filePath, body, 'utf8', (writeError) => {
      if (writeError) {
        console.error(writeError);
      } else {
        console.log('File writen successful.');
      }
    });
  }
});
