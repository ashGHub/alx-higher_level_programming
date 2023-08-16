#!/usr/bin/node
const dct = require('./101-data').dict;
const result = {};
for (const userId in dct) {
  const ocr = dct[userId];
  if (!result[ocr]) {
    result[ocr] = [];
  }
  result[ocr].push(userId);
}
console.log(result);
