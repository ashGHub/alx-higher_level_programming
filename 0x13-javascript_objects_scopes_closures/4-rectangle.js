#!/usr/bin/node
class Rectangle {
  width;
  height;
  cr = 'X';

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
        rw = this.cr + rw;
      }
      console.log(rw);
    }
  }

  rotate () {
    const tmp = this.width;
    this.width = this.height;
    this.height = tmp;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}
module.exports = Rectangle;
