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
      // Fetch all character names in the same order as they appear in the "characters" list
      const characterNames = [];
      let completedRequests = 0;

      data.characters.forEach((characterUrl, index) => {
        request.get(characterUrl, (error, response, body) => {
          if (error) {
            console.error('Error:', error);
          } else {
            // Parse the character data
            const characterData = JSON.parse(body);
            // Store the character name in the correct index
            characterNames[index] = characterData.name;

            // Increment the count of completed requests
            completedRequests++;

            // Print the character names when all have been retrieved
            if (completedRequests === data.characters.length) {
              characterNames.forEach(name => console.log(name));
            }
          }
        });
      });
    } else {
      console.error('No characters found for this movie.');
    }
  }
});
