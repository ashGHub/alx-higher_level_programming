#!/usr/bin/node
const request = require('request');
const url = `https://swapi-api.hbtn.io/api/films/${process.argv[2]}`;

request(url, function (err, response, body) {
  if (err) {
    return console.log(err);
  }
  const movieData = JSON.parse(body);
  const characters = movieData.characters;

  const characterPromises = characters.map((characterUrl) => {
    return new Promise((resolve, reject) => {
      request(characterUrl, (error, response, body) => {
        if (error) {
          reject(error);
        } else {
          const characterData = JSON.parse(body);
          resolve(characterData.name);
        }
      });
    });
  });

  // wait for all promises to resolve to keep the order
  Promise.all(characterPromises)
    .then((characterNames) => {
      characterNames.forEach((name) => {
        console.log(name);
      });
    })
    .catch((error) => {
      console.error(error);
    });
});
