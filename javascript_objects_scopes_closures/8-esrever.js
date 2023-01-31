#!/usr/bin/node
const esrever = (list) => {
  const newList = [];
  for (let m = list.length - 1; m >= 0; m--) {
    newList.push(list[m]);
  }
  return newList;
};

exports.esrever = esrever;
