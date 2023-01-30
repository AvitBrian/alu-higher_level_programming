#!/usr/bin/node
const [a,b, ...args] = process.argv

if (args == 0){
    console.log('No argument')
}else {console.log(...args)}
