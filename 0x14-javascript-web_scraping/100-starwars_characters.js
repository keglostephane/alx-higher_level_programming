#!/usr/bin/node
/* Print all character of a Star Wars movie */

const path = require('node:path');
const args = process.argv;
const request = require('request');

if (args.length === 3) {
  const filmId = parseInt(args[2], 10);
  const filmUrl = `https://swapi-api.alx-tools.com/api/films/${filmId}/`;

  request.get(filmUrl, (error, response, body) => {
    if (error) {
      console.log(error);
    } else {
      const film = JSON.parse(body);
      for (const url of film.characters) {
        request.get(url, (error, response, body) => {
          if (error) {
            console.log(error);
          } else {
            const person = JSON.parse(body);
            console.log(person.name);
          }
        });
      }
    }
  });
} else {
  console.log(`Usage ./${path.basename(args[1])}\
 <Film Id>`);
}
