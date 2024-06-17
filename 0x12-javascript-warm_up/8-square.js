#!/usr/bin/node
const args = process.argv.slice(2);
const sizes = parseInt(args[0], 10);

if (isNaN(sizes) || sizes <= 0) {
  console.log('Missing size');
} else {
  const lines = 'X'.repeat(sizes);
  for (let u = 0; u < sizes; u++) {
    console.log(lines);
  }
}
