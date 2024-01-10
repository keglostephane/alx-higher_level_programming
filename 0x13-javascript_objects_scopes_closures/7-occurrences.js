#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let n = 0;
  if (list && list.length > 0) {
    for (const val of list) {
      if (val === searchElement) {
        n++;
      }
    }
    return n;
  } else {
    return 0;
  }
};
