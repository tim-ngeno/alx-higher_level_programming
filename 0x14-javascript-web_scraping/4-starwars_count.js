#!/usr/bin/node
const request = require('request');

if (process.argv.length <= 2) {
  console.error('Provide the Star Wars API URL');
  process.exit(1);
}

const endpoint = process.argv[2];
const characterId = '18';

request(endpoint, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const films = JSON.parse(body).results;

    let count = 0;
    films.forEach(film => {
      if (film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)) {
        count += 1;
      }
    });

    console.log(count);
  }
});
