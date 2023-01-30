#!/usr/bin/node
const [,, a] = process.argv;
if (a.isNaN) {
  console.log('Not a number');
} else {
  console.log(`My number: ${a}`);
}
