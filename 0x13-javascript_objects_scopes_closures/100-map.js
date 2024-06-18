#!/usr/bin/node
const list = require('./100-data.js').list;

const anewList = list.map((vl, inx) => vl * inx);
console.log(list);
console.log(anewList);
