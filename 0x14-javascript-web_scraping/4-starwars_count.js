#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const wedgeAntillesId = '18';

request(url, function (err, response, body) {
  if (err) {
    return console.log(err);
  }
  let count = 0;
  const films = JSON.parse(body).results;
  for (const film of films) {
    for (const character of film.characters) {
      if (character.includes(`/${wedgeAntillesId}/`)) {
        count++;
      }
    }
  }
  console.log(count);
});
