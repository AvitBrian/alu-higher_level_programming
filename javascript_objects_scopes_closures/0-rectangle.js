#!/usr/bin/node
class Rectangle {
  constructor (...a) {
    this.a = a
  }
}

const r1 = new Rectangle ()
console.log(r1)
exports.Rectangle = Rectangle;
