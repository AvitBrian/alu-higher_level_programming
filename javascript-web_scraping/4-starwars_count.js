#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    let count = 0;
    const file = JSON.parse(body).results;
    console.log(file);
    for (const data in file) {
      const charlist = file[data].characters;
      for (const each in charlist) {
        if (charlist[each].includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
