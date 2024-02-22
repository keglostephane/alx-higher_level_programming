#!/usr/bin/node
/* Prints the title of a Star Wars movie */

const path = require('node:path');
const args = process.argv;
const request = require('request');

if (args.length === 3) {
  const id = parseInt(args[2], 10);
  const endpoint = `https://swapi-api.alx-tools.com/api/films/${id}`;

  request.get(endpoint, (error, response, body) => {
    if (error) {
      console.log(error);
    } else {
      const film = JSON.parse(body);
      console.log(film.title);
    }
  });
} else {
  console.log('Usage ./%s <film_id>', path.basename(args[1]));
}
