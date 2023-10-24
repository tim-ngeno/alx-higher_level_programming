#!/usr/bin/node
const request = require('request');

if (process.argv.length !== 3) {
  console.error('Provide the Movie ID');
  process.exit(1);
}

const movieId = process.argv[2];
const movieEndpoint = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(movieEndpoint, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const movie = JSON.parse(body);
    const characterUrls = movie.characters;

    for (const url of characterUrls) {
      request(url, (err, resp, charBody) => {
        if (!err && resp.statusCode === 200) {
          const character = JSON.parse(charBody);
          console.log(character.name);
        }
      });
    }
  } else {
    console.error("Couldn't get movie data from API");
  }
});
