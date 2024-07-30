#!/usr/bin/node
const fs = require('fs');

// Get the file path and string to write from the command line arguments
const filePath = process.argv[2];
const content = process.argv[3];

// Write the string to the file in UTF-8 encoding
fs.writeFile(filePath, content, 'utf8', (err) => {
  if (err) {
    // Print the error object if an error occurred
    console.error(err);
  }
});
