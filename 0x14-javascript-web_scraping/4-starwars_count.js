#!/usr/bin/node
const request = require('request');

if (process.argv.length <= 2) {
  console.error('Provide the Star Wars API URL');
  process.exit(1);
}

const endpoint = process.argv[2];

request(endpoint, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const films = JSON.parse(body).results;

    const count = 0;
    films.forEach(film => {
      if (film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')) {
        count += 1;
      }
    });

    console.log(count);
  } else {
    console.log(error);
  }
});
