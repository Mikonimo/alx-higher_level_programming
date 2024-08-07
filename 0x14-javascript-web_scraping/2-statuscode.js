#!/usr/bin/node
const request = require('request');

// Get the URL from the command line arguments
const url = process.argv[2];

// Send a GET request to the URL
request.get(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else {
    // Print the status code
    console.log(`code: ${response.statusCode}`);
  }
});
