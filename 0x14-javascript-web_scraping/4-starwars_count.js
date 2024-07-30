#!/usr/bin/node
const request = require('request');

// Get the API URL from the command line arguments
const apiUrl = process.argv[2];

// Character ID for Wedge Antilles
const wedgeAntillesId = 18;

// Send a GET request to the API URL
request.get(apiUrl, (response, body) => {
    // Parse the JSON response
    const data = JSON.parse(body);
    // Check if the results exist in the response
    if (data.results) {
      // Filter the movies where Wedge Antilles is present
      const wedgeMovies = data.results.filter(film =>
        film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${wedgeAntillesId}/`)
      );

      // Print the number of movies
      console.log(wedgeMovies.length);
    } else {
      console.error('No movies found');
    }
});
