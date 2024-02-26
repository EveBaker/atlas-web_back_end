const http = require('http');

// Create server
const app = http.createServer((req, res) => {
  // Set headers
  res.writeHead(200, { 'Content-Type': 'text/plain' });
  
  // Send
  res.end('Hello Holberton School!\n');
});

// Listen on port 
const PORT = 1245;
app.listen(PORT, () => {
  console.log(`Server is running and listening on port ${PORT}`);
});

// Export the server
module.exports = app;