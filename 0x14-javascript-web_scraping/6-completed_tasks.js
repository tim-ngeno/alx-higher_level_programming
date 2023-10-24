#!/usr/bin/node
const request = require('request');

if (process.argv.length !== 3) {
  console.error('Usage: ./6-completed_tasks.js <API_URL>');
  process.exit(1);
}

const url = process.argv[2];

request(url, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const todos = JSON.parse(body);

    const tasksByUser = {};

    for (const task of todos) {
      if (task.completed) {
        if (tasksByUser[task.userId]) {
          tasksByUser[task.userId] += 1;
        } else {
          tasksByUser[task.userId] = 1;
        }
      }
    }

    console.log(tasksByUser);
  }
});
