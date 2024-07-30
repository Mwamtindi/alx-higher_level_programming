#!/usr/bin/node
const fs = require('fs');

// Get file path and string to write from command line arguments
const filePath = process.argv[2];
const content = process.argv[3];

fs.writeFile(filePath, content, 'utf-8', (errr) => {
  if (errr) {
    console.error(errr);
  }
});
