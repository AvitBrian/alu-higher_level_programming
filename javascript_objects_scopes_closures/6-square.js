#!/usr/bin/node
const newSquare = require('./5-square.js');

module.exports = class Square extends newSquare {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let m = 0; m < this.height; m++) {
        console.log('C'.repeat(this.width));
      }
    }
  }
};
