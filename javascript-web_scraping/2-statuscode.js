#!/usr/bin/node
import { request } from 'request';
const url = process.argv[2];

request(url, (err, res) => {
  if (err) {
    console.log(err);
  } else {
    console.log('code:', res.statusCode);
  }
});
