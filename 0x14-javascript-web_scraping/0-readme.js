#!/usr/bin/node
/* Read the content of a file */

const fs = require('node:fs');
const path = require('node:path');
const args = process.argv;

if (args.length === 3) {
  fs.readFile(args[2], 'utf-8', (err, data) => {
    if (err) {
      console.error(err);
      return;
    }
    console.log(data);
  });
} else {
  console.log('Usage: ./%s <filename>', path.basename(args[1]));
}
