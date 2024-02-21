#!/usr/bin/node
/* Display the status code of a GET request */

const path = require('node:path');
const args = process.argv;
const request = require('request');

if (args.length === 3) {
  const url = args[2];
  request(url, (error, response, body) => {
    if (error) {
      console.log(error);
    } else {
      console.log('code: %i', response.statusCode);
    }
  });
} else {
  console.log('Usage: ./%s <url>', path.basename(args[1]));
}
