#!/usr/bin/node
const fs = require('fs');

if (process.argv.length <= 2) {
  console.error('provide a file path as an argument');
  process.exit(1);
}

const filePath = process.argv[2];

fs.readFile(filePath, 'utf-8', (error, content) => {
  if (error) {
    console.error(error);
  } else {
    console.log(content);
  }
});
