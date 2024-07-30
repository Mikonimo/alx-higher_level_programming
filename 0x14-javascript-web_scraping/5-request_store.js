#!/usr/bin/node
const request = require('request');
const fs = require('fs');

// Get the URL and file path from the command line arguments
const url = process.argv[2];
const filePath = process.argv[3];

// Send a GET request to the URL
request.get(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else {
    // Write the response body to the file in UTF-8 encoding
    fs.writeFile(filePath, body, 'utf8', (err) => {
      if (err) {
        console.error('Error:', err);
      } else {
        console.log(`Content saved to ${filePath}`);
      }
    });
  }
});
