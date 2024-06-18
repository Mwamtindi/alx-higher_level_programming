#!/usr/bin/node
const PrevSquareCls = require('./5-square');

class Square extends PrevSquareCls {
  charPrint (c) {
    const myCharSqr = c === undefined ? 'X' : c;
    for (let u = 0; u < this.height; u++) {
      let myVarSqr = '';
      let q = 0;
      while (q < this.width) {
        myVarSqr += myCharSqr;
        q++;
      }

      console.log(myVarSqr);
    }
  }
}

module.exports = Square;
