#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let occurr = 0;

  for (let u = 0; u < list.length; u++) {
    occurr = (list[u] === searchElement ? occurr + 1 : occurr);
  }

  return occurr;
};
