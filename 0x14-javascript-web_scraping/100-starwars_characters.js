#!/usr/bin/node
/* Print all character of a Star Wars movie */

const path = require('node:path');
const args = process.argv;
const request = require('request');

if (args.length === 3) {
  const filmId = args[2];
  const filmUrl = `https://swapi-api.alx-tools.com/api/films/${filmId}/`;
  const url = 'https://swapi-api.alx-tools.com/api/people';

  request.get(url, (error, response, body) => {
    if (error) {
      console.log(error);
    } else {
      const people = JSON.parse(body).results;
      for (const person of people) {
        for (const film of person.films) {
          if (film === filmUrl) console.log(person.name);
        }
      }
    }
  });
} else {
  console.log(`Usage ./${path.basename(args[1])}\
 <Film Id>`);
}
