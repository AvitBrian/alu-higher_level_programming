#!/usr/bin/node
const [,, ...args] = process.argv;

if (args == 0) {
  console.log('No argument');
} else { console.log(...args); }
