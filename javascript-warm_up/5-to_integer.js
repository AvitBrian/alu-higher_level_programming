#!/usr/bin/node
const [,, a] = process.argv;
if (parseInt(a).isNaN) {
  console.log('Not a number');
} else {
  console.log(`My number: ${a}`);
}
