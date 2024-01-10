#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let str = '';
    for (let i = 0; i < this.width; i++) {
      str += 'X';
    }
    for (let j = 0; j < this.height; j++) {
      console.log(str);
    }
  }

  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

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
