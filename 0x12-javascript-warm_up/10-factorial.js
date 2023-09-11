#!/usr/bin/node

const arg = parseInt(process.argv[2]);

function factorial (n) {
  if (n === 0 || n === 1 || isNaN(n)) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

if (!isNaN(arg)) {
  console.log(factorial(arg));
} else {
  console.log(1);
}
