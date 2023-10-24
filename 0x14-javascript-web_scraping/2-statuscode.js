#!/usr/bin/node
const request = require('request');

if (process.argv.length <= 2) {
  console.error('Provide a URL address');
  process.exit(1);
}

const url = process.argv[2];

request(url, (error, response) => {
  if (error) {
    console.log(error);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
