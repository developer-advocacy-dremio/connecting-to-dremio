// Import Dependencies and Load .env into process.env
require("dotenv").config();
const axios = require("axios");

// setup credentials
const controlPlane = "https://api.dremio.cloud/v0";
const token = process.env.personalKey;
const projectID = process.env.projectID;

//setup endpoint
const endpoint = `/projects/${projectID}/sql`;
const request_url = controlPlane + endpoint;

// Setup headers and body of request
const headers = {
  authorization: `bearer ${token}`,
  "Content-Type": "application/json",
};

const data = JSON.stringify({
  sql: 'SELECT * FROM \\"nyc-taxi-data\\" limit 100',
  context: ["@dremio.demo@gmail.com"],
});

// Make request
const response = axios({
  method: "post",
  url: request_url,
  headers,
  data,
});

// process request when complete
response.then((results) => {
    console.log(results.data)
})
