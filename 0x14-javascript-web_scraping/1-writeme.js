#!/usr/bin/node
const fs = require('fs');

// Get file path and string to write from command line arguments
const filePath = process.argv[2];
const content = process.argv[3];

if (!filePath || !content) {
  console.error('Usage: ./1-writeme.js <file_path> <content>');
  process.exit(1);
}

// Write the string to the file
fs.writeFile(filePath, content, 'utf-8', (err) => {
  if (err) {
    console.error(err);
  } else {
    console.log(`Content written to ${filePath}`);
  }
});
