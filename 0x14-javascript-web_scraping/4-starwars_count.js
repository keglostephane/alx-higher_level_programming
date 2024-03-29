#!/usr/bin/node
/* Print the number of movies where the character
"Wedge Antilles" is present */

const path = require('node:path');
const args = process.argv;
const request = require('request');

if (args.length === 3) {
  const endpoint = args[2];

  request.get(endpoint, (error, response, body) => {
    if (error) {
      console.log(error);
    } else {
      const films = JSON.parse(body).results;
      let count = 0;
      for (const film of films) {
        for (const character of film.characters) {
          if (character.endsWith('18/')) count += 1;
        }
      }
      console.log(count);
    }
  });
} else {
  console.log(`Usage ./${path.basename(args[1])}\
 <https://swapi-api.alx-tools.com/api/films/>`);
}
