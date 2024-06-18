#!/usr/bin/node
const dict = require('./101-data.js').dict;
const occurDict = {};

for (const key in dict) {
  if (occurDict[dict[key]] === undefined) {
    occurDict[dict[key]] = [key];
  } else {
    occurDict[dict[key]].push(key);
  }
}
console.log(occurDict);
