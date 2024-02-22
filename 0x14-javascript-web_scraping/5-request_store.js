#!/usr/bin/node
/* Write the content of webpage to a file */

const fs = require('node:fs');
const path = require('node:path');
const request = require('request');
const args = process.argv;

if (args.length === 4) {
  const url = args[2];
  const filename = args[3];

  request.get(url, (error, response, body) => {
    if (error) console.log(error);
    else {
      const content = body;
      fs.writeFile(filename, content, 'utf-8', err => {
        if (err) console.log(err);
      });
    }
  });
} else console.log(`Usage: ./${path.basename(args[1])} <url> <filename>`);
