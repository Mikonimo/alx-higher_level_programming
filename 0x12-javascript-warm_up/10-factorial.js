#!/usr/bin/node

// Recursive function to compute factorial
const factorial = n => {
  if (n <= 1) {
    return 1;
  }
  return n * factorial(n - 1);
};

const args = process.argv;
const num = parseInt(args[2], 10);

// Compute and print the factorial
console.log(factorial(isNaN(num) ? 1 : num));
