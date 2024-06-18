#!/usr/bin/node

let countArg = 0;

exports.logMe = function numArg (item) {
  console.log(`${countArg}: ${item}`);
  countArg += 1;
};
