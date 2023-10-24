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
    printCharacters(characterUrls, 0);
  } else {
    console.error(error);
  }
});

function printCharacters (characterUrls, index) {
  if (index >= characterUrls.length) {
    return;
  }

  request(characterUrls[index], (err, res, data) => {
    if (!err && res.statusCode === 200) {
      const character = JSON.parse(data);
      console.log(character.name);
      printCharacters(characterUrls, index + 1);
    }
  });
}
