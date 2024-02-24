const express = require('express');
const app = express();

app.get('/', (req, res) => {
    res.send('Welcome to the payment system');
});

const PORT = 7865;
app.listen(PORT, () => {
    console.log('API avalableon localhost port ${PORT}');
});

module.exports = app;