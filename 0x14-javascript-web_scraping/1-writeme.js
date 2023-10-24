#!/usr/bin/node
const fs = require('fs');

if (process.argv.length <= 3) {
  console.log('Usage: ./1-writeme.js <file_path> <input_text>');
  process.exit(1);
}

const filePath = process.argv[2];
const content = process.argv[3];

fs.writeFile(filePath, content, 'utf-8', (error) => {
  if (error) {
    console.error(error);
  }
});
