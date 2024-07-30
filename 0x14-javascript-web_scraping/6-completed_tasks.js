#!/usr/bin/node

const request = require('request');

// Get the API URL from the command line arguments
const apiUrl = process.argv[2];

if (!apiUrl) {
  console.error('Error: The API URL not provided.');
  process.exit(1);
}

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    if (response.statusCode === 200) {
      const todos = JSON.parse(body);
      const completedTasksByUser = {};

      todos.forEach((todo) => {
        if (todo.completed) {
          if (completedTasksByUser[todo.userId]) {
            completedTasksByUser[todo.userId]++;
          } else {
            completedTasksByUser[todo.userId] = 1;
          }
        }
      });

      console.log(completedTasksByUser);
    } else {
      console.error(`Error: Failed to retrieve the data. Status code: ${response.statusCode}`);
    }
  }
});
