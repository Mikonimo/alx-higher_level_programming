#!/usr/bin/node

// Function to add two numbers
const add = (a, b) => a + b;

const args = process.argv;
const num1 = parseInt(args[2], 10);
const num2 = parseInt(args[3], 10);

// Check if both arguments are valid numbers
if (isNaN(num1) || isNaN(num2)) {
  console.log('NaN');
} else {
  console.log(add(num1, num2));
}
