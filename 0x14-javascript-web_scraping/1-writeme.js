#!/usr/bin/node
// Writes a String to a file

const fs = require('fs');

if (process.argv.length <= 3) {
  console.log('Usage: <program> <file_path> <text>');
  process.exit(1);
}

const content = process.argv[3];
const filePath = process.argv[2];

fs.writeFile(filePath, content, (error) => {
  if (error) {
    console.error(error);
  } else {
    console.log('Save success!');
  }
});
