#!/usr/bin/node

const request = require('request');

// Get URL from command line arguments
const url = process.argv[2];

if (!url) {
  console.error('Usage: ./2-statuscode.js <url>');
  process.exit(1);
}

// Perform GET request
request.get(url, (error, response) => {
  if (error) {
    console.error('Error:', error);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
