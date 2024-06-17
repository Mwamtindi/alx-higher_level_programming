#!/usr/bin/node
const args = process.argv.slice(2);
const numx = parseInt(args[0], 10);

if (isNaN(numx) || numx <= 0) {
  console.log('Missing number of occurrences');
} else {
  for (let u = 0; u < numx; u++) {
    console.log('C is fun');
  }
}
