#!/usr/bin/node

const args = process.argv.slice(2).map(Number);

if (args.length <= 1) {
  console.log(0);
} else {
  let firstMax = -Infinity;
  let secondMax = -Infinity;

  for (const num of args) {
    if (num > firstMax) {
      secondMax = firstMax;
      firstMax = num;
    } else if (num > secondMax && num !== firstMax) {
      secondMax = num;
    }
  }

  console.log(secondMax !== -Infinity ? secondMax : 0);
}
