#!/usr/bin/node

const n = parseInt(process.argv[2]);

function factorial (n) {
  if (!n) {
    return 1;
  }
  return n < 2 ? 1 : n * factorial(n - 1);
}

console.log(factorial(n));
