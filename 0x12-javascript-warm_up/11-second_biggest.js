#!/usr/bin/node

const args = process.argv;
const list = args.slice(2);

if ((args.length === 2) || (args.length === 3)) {
  console.log(0);
} else {
  for (let i = 0; i < list.length; i++) {
    list[i] = parseInt(list[i]);
  }
  console.log(list.sort((a, b) => a - b)[list.length - 2]);
}
