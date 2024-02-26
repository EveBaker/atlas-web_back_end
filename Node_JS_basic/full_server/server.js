const express = require('express');

const app = express();
const routes = require('./routes/index.js');

app.use('/', routes);

const PORT = 1245;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));

module.exports = app; // Export for testing purposes
