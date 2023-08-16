#!/usr/bin/node
const fs = require('fs');

fs.readFile(process.argv[2], 'utf8', (err, dataA) => {
  if (err) {
    console.log(err);
  }
  fs.readFile(process.argv[3], 'utf8', (err, dataB) => {
    if (err) {
      console.log(err);
    }
    fs.writeFile(process.argv[4], dataA + dataB, (err) => {
      if (err) {
        console.log(err);
      }
    });
  });
});
