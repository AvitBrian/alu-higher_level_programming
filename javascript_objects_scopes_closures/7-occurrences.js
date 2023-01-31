#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  for (const m in list) {
    if (list[m] === searchElement) {
      count++;
    }
  }
  return count;
};
