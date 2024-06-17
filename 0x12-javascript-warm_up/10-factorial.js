#!/usr/bin/node
const args = process.argv.slice(2);

function factorialc (n) {
  if (isNaN(n) || n <= 1) {
    return 1;
  }
  return n * factorialc(n - 1);
}

const number = parseInt(args[0], 10);
console.log(factorialc(number));
