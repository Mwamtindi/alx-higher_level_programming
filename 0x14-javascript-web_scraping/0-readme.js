#!/usr/bin/node
const fs = require('fs');

// Get the file path from command line arguments
const filePath = process.argv[2];

if (!filePath) {
  console.error('Please provide a file path as an argument.');
  process.exit(1);
}

// Read the file and handle any errors
fs.readFile(filePath, 'utf-8', (err, data) => {
  if (err) {
    console.error(err);
  } else {
    console.log(data);
  }
});
