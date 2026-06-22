#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + movieId + '/';

request(url, function (err, res, body) {
  if (err) return;
  const characters = JSON.parse(body).characters;

  function fetchCharacter (index) {
    if (index >= characters.length) return;
    request(characters[index], function (err, res, body) {
      if (err) return;
      console.log(JSON.parse(body).name);
      fetchCharacter(index + 1);
    });
  }

  fetchCharacter(0);
});
