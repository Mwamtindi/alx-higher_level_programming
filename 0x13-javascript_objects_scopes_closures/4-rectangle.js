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

  rotate () {
    let tempr = 0;
    tempr = this.width;
    this.width = this.height;
    this.height = tempr;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}
module.exports = Rectangle;
