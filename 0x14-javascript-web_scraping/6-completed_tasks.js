#!/usr/bin/node
const request = require('request');

// Get the API URL from the command line arguments
const apiUrl = process.argv[2];

// Send a GET request to the API URL
request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else {
    // Parse the JSON response
    const data = JSON.parse(body);

    // Initialize an object to store the count of completed tasks by user
    const completedTasks = {};

    // Iterate through the tasks and count the completed ones by user
    data.forEach(task => {
      if (task.completed) {
        if (!completedTasks[task.userId]) {
          completedTasks[task.userId] = 0;
        }
        completedTasks[task.userId]++;
      }
    });

    // Print the result
    console.log(completedTasks);
  }
});
