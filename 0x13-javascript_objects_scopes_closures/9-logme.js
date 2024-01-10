#!/usr/bin/node

const logMe = function (item) {
  let nb = 0;
  return function increment (item) {
    console.log('%d: %s', nb++, item);
  };
};

exports.logMe = logMe();
