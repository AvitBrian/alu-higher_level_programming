#!/usr/bin/node
const request = require('request');
const episodeId = process.argv[2];
const API = 'https://swapi-api.alx-tools.com/api/films/'+ episodeId;

request(API, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const data = JSON.parse(body);
    console.log(data.title)
  }
});
