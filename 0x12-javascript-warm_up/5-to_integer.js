#!/usr/bin/node
const args = process.argv.slice(2);
const numb = Number(args[0]);

if (!isNaN(numb) && Number.isInteger(numb)) {
  console.log(`My number: ${numb}`);
} else {
  console.log('Not a number');
}
