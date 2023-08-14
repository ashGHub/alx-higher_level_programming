#!/usr/bin/node

const a = parseInt(process.argv[2]);
const b = parseInt(process.argv[3]);

if ((a === 0 || a) && (b === 0 || b)) {
  console.log(add(a, b));
} else {
  console.log('NaN');
}

function add (a, b) {
  return a + b;
}
