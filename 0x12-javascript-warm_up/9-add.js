#!/usr/bin/node
const args = process.argv.slice(2);

function addi (a, b) {
  return a + b;
}

const a = parseInt(args[0], 10);
const b = parseInt(args[1], 10);

if (isNaN(a) || isNaN(b)) {
  console.log('NaN');
} else {
  console.log(addi(a, b));
}
