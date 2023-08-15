#!/usr/bin/node

const Sq = require('./5-square');

class Square extends Sq {
  charPrint (c) {
    if (c) {
      super.cr = c;
    }
    super.print();
  }
}
module.exports = Square;
