#!/usr/bin/node

// Define the function add
function add (a, b) {
  return a + b;
}

// Export the add function to make it visible outside the module
module.exports.add = add;
