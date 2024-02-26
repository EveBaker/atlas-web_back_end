const http = require('http');

//create server
const app = http.createServer((req, res) => {
//set
res.writeHead(200, { 'Content-Type': 'text/plain' });

//send
res.end('Hello Holberton School!\n');
});

//listen on port
const PORT = 1245;
app.listen(PORT, () => {
    console.log(`Server is running and listening on port ${PORT}`);
});

module.exports = app;