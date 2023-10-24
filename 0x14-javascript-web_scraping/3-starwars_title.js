#!/usr/bin/node
const request = require('request');

if (process.argv.length <= 2) {
  console.error('Provide the Movie ID');
  process.exit(1);
}

const movie_id = process.argv[2];
const endpoint = `https://swapi-api.alx-tools.com/api/films/${movie_id}`;

request(endpoint, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const data = JSON.parse(body);
    console.log(data.title);
  }
});
