#!/usr/bin/node
const request = require('request');

// Get the Movie ID from the command line arguments
const movieId = process.argv[2];

// Construct the URL for the API request
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Send a GET request to the URL
request.get(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else {
    // Parse the JSON response
    const data = JSON.parse(body);

    // Check if characters exist in the response
    if (data.characters) {
      // Iterate through the character URLs and fetch their names
      data.characters.forEach(characterUrl => {
        request.get(characterUrl, (error, response, body) => {
          if (error) {
            console.error('Error:', error);
          } else {
            // Parse the character data
            const characterData = JSON.parse(body);
            // Print the character name
            console.log(characterData.name);
          }
        });
      });
    } else {
      console.error('No characters found for this movie.');
    }
  }
});
