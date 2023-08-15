#!/usr/bin/node
const lst = require('./100-data').list;
console.log(lst);
console.log(lst.map(function (n, i) {
  return n * i;
}));
