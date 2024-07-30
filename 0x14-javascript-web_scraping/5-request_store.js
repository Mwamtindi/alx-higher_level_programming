#!/usr/bin/node

const request = require('request');
const fs = require('fs');

// Get URL and file path from command line arguments
const url = process.argv[2];
const filePath = process.argv[3];

if (!url || !filePath) {
  console.error('Usage: ./5-savewebpage.js <url> <file_path>');
  process.exit(1);
}

// Perform GET request to the URL
request.get(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    process.exit(1);
  }

  // Write response body to the file
  fs.writeFile(filePath, body, 'utf-8', (err) => {
    if (err) {
      console.error('Error writing to file:', err);
      process.exit(1);
    } else {
      console.log(`Content saved to ${filePath}`);
    }
  });
});
