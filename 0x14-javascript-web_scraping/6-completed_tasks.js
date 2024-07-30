#!/usr/bin/node

const request = require('request');

// Get API URL from the command line arguments
const apiUrl = process.argv[2];

if (!apiUrl) {
  console.error('Usage: ./6-taskcount.js <api_url>');
  process.exit(1);
}

// Fetch tasks from the API
request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    process.exit(1);
  }

  const tasks = JSON.parse(body);
  const userTaskCount = {};

  // Count completed tasks by user ID
  tasks.forEach(task => {
    if (task.completed) {
      if (!userTaskCount[task.userId]) {
        userTaskCount[task.userId] = 0;
      }
      userTaskCount[task.userId]++;
    }
  });

  // Print users with at least one completed task
  Object.entries(userTaskCount).forEach(([userId, count]) => {
    console.log(`User ${userId}: ${count} completed tasks`);
  });
});
