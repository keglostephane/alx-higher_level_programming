#!/usr/bin/node

const dict = require('./101-data.js').dict;

const userIdByOccurence = Object.keys(dict).reduce((newDict, index) => {
  const occur = dict[index];
  const key = String(occur);

  if (!newDict[key]) {
    newDict[key] = [];
  }

  newDict[key].push(index);
  return (newDict);
}, {});

console.log(userIdByOccurence);
