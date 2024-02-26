const express = require('express');
const app = express();

app.use(express.json());

app.get('/', (req, res) => {
    res.send('Welcome to the payment system');
});

app.get('/available_payments', (req, res) => {
    res.json({
        payment_methods: {
            credit_cards: true,
            paypal: false
        }
    });
});

app.post('/login', (res, req) => {
    const { userName } = req.body;
    res.send(`Welcome ${userName}`);
});

const PORT = 7865;
app.listen(PORT, () => {
    console.log('API avalable on localhost port ${PORT}');

    app.get('/cart/:id(\\d+)', (req, res) => {
        const { id } = req.params;
        res.send(`Payment methods for cart ${id}`);
      });
});


module.exports = app;