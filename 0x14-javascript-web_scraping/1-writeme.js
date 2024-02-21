#!/usr/bin/node
/* Write a string to a file */

const fs = require('node:fs');
const path = require('node:path');
const args = process.argv;

if (args.length === 4) {
  const filename = args[2];
  const content = args[3];

  fs.writeFile(filename, content, 'utf-8', err => {
    if (err) {
      console.log(err);
    }
  });
} else {
  console.log('Usage: ./%s <filename> <content>', path.basename(args[1]));
}
