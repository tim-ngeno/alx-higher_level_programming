#!/usr/bin/node

// Get an array of arguments passed
const args = process.argv.slice(2);

if (args.length === 0 || args.length === 1) {
  console.log(0);
} else {
  // Convert the array items to integers and filter non-integers
  const integers = args.map(Number).filter(Number.isInteger);

  // Sort in descending order
  const sorted = integers.sort((a, b) => b - a);

  if (sorted.length < 2) {
    console.log(0);
  } else {
    console.log(sorted[1]);
  }
}
