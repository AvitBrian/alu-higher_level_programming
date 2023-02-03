#!/usr/bin/node
const newSquare = require('./5-square.js');

module.exports = class Square extends newSquare {
  charPrint (c) {
    if (c === undefined) {
      for (let m = 0; m < this.height; m++) {
        console.log('X'.repeat(this.width));
      }
    } else {
      for (let m = 0; m < this.height; m++) {
        console.log(c.repeat(this.width));
      }
    }
  }
};
