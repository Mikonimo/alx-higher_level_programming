#!/usr/bin/node
const request = require('request');

// Get the movie ID from the command line arguments
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

    // Check if the title exists in the response
    if (data.title) {
      console.log(data.title);
    } else {
      console.error('Movie not found');
    }
  }
});
