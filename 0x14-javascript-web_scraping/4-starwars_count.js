#!/usr/bin/node
const request = require('request');

if (process.argv.length <= 2) {
  console.error('Provide the Star Wars API URL');
  process.exit(1);
}

const endpoint = process.argv[2];

request(endpoint, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const count = body.split('/people/18/').length - 1;
    console.log(count);
  } else {
    console.log(error);
  }
});
