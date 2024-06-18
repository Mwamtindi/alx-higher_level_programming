#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (typeof w === 'number' && w > 0 && typeof h === 'number' && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let u = 0; u < this.height; u++) {
      let myVarRec = '';
      let g = 0;
      while (g < this.width) {
        myVarRec += 'X';
        g++;
      }

      console.log(myVarRec);
    }
  }
}
module.exports = Rectangle;
