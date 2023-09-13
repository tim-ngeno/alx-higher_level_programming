#!/usr/bin/node

const fs = require('fs');

const source1 = process.argv[2];
const source2 = process.argv[3];
const dest = process.argv[4];

fs.readFile(source1, 'utf-8', (err, content1) => {
  if (err) process.exit(1);

  fs.readFile(source2, 'utf-8', (err, content2) => {
    if (err) process.exit(1);

    const concatData = content1 + content2;

    fs.writeFile(dest, concatData, 'utf-8', (err) => {
      if (err) process.exit(1);
    });
  });
});
