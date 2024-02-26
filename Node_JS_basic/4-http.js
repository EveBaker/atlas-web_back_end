const http = require('http');

// Create server
const app = http.createServer((req, res) => {
  // Set headers
  res.writeHead(200, { 'Content-Type': 'text/plain' });

  // Send
  res.end('Hello Holberton School!\n');
});

// Listen on port
app.listen(1245);

// Export the server
module.exports = app;
