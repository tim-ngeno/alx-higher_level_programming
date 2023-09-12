#!/usr/bin/node

const data = require('./101-data').dict;

const users = {};

for (const userId in data) {
  const occurrence = data[userId];

  if (!users[occurrence]) {
    users[occurrence] = [];
  }

  users[occurrence].push(userId);
}

console.log(users);
