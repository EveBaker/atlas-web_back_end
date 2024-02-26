//import redis
import redis from 'redis';

//create
const client = redis.createClient();

//listens for connect
client.on('connect', () => {
    console.log('Redis client connected to the server');
});


//listens for error
client.on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err.message}`);
});