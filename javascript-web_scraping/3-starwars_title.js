#!/usr/bin/node
const request = require('request');
const movieID = process.argv[2];
const API = 'https://swapi-api.alx-tools.com/api/films/' + movieID;

request(API, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const data = JSON.parse(body);
    console.log(data);
  }
});
