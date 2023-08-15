#!/usr/bin/node
class Rectangle {
  width;
  height;

  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let rw = '';
      for (let j = 0; j < this.width; j++) {
        rw = 'X' + rw;
      }
      console.log(rw);
    }
  }
}
module.exports = Rectangle;
