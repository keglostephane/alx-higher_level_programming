#!/usr/bin/node

const Square1 = require('./5-square');

class Square extends Square1 {
  charPrint (c) {
    if (c) {
      let str = '';
      for (let i = 0; i < this.width; i++) {
        str += c;
      }
      for (let j = 0; j < this.height; j++) {
        console.log(str);
      }
    } else {
      super.print();
    }
  }
}

module.exports = Square;
