#!/usr/bin/node

const n = parseInt(process.argv[2]);

if (Number.isInteger(parseInt(n))) {
  for (let i = 0; i < n; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
