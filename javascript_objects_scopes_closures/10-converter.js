#!/usr/bin/node
const converter = function (base) {
  return (number) => number.toString(base);
};

exports.converter = converter;
