#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

const completed = {};
request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const file = JSON.parse(body);
    for (const data of file) {
      if (data.completed === true) {
        if (completed[data.userId]) {
          completed[data.userId]++;
        } else {
          completed[data.userId] = 1;
        }
      }
    }
    console.log(completed);
  }
});
