#!/usr/bin/node
/* Compute the number of tasks completed by user id */

const path = require('node:path');
const args = process.argv;
const request = require('request');

if (args.length === 3) {
  const url = args[2];

  request.get(url, (error, response, body) => {
    if (error) console.log(error);
    else {
      const users = JSON.parse(body);
      const dict = new Map();
      for (const user of users) {
        if (dict.get(user.userId)) {
          if (user.completed) {
            dict.set(user.userId,
              dict.get(user.userId) + 1);
          }
        } else {
          if (user.completed) dict.set(user.userId, 1);
          else dict.set(user.userId, 0);
        }
      }
      const obj = Object.fromEntries(dict);
      console.log(obj);
    }
  });
} else {
  console.log(`Usage ./${path.basename(args[1])}\
<https://jsonplaceholder.typicode.com/todos>`);
}
