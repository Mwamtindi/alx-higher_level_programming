#!/usr/bin/node
const args = process.argv.slice(2);
const numx = parseInt(args[0], 10);

if (isNaN(numx)) {
  console.log('Missing number of occurrences');
} else {
  let count = 0;
  while (count < numx) {
    console.log('C is fun');
    count++;
  }
}
