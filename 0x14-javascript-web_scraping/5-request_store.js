#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const file = process.argv[3];

request.get(url, function (err, response, body) {
  if (err) {
    return console.log(err);
  }
  fs.writeFile(file, body, 'utf-8', function (err) {
    if (err) {
      return console.log(err);
    }
  });
});
