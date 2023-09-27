#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, function (err, response, body) {
  if (err) {
    return console.log(err);
  }
  const completedTasks = {};
  for (const task of JSON.parse(body)) {
    if (task.completed === true) {
      if (completedTasks[task.userId] === undefined) {
        completedTasks[task.userId] = 1;
      } else {
        completedTasks[task.userId]++;
      }
    }
  }
  console.log(completedTasks);
});
