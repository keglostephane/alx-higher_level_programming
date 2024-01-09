#!/usr/bin/node

const arg1 = parseInt(process.argv[2]);
let str = '';

if (arg1) {
  for (let i = 0; i < arg1; i++) {
    for (let j = 0; j < arg1; j++) {
      str += 'X';
    }
    console.log(str);
    str = '';
  }
} else {
  console.log('Missing size');
}
