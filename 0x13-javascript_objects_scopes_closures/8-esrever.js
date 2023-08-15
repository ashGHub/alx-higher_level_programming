#!/usr/bin/node
exports.esrever = function (list) {
  const result = list;

  for (let i = 0, j = list.length - 1; i < j; i++, j--) {
    const tmp = result[i];
    result[i] = result[j];
    result[j] = tmp;
  }
  return result;
};
