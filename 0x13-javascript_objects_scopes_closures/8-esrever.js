#!/usr/bin/node

exports.esrever = function (list) {
  const reversedVerList = [];
  for (let u = list.length - 1; u >= 0; u--) {
    reversedVerList.push(list[u]);
  }

  return (reversedVerList);
};
