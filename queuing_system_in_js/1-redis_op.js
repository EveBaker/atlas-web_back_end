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

//set new school
function setNewSchool(schoolName, value) {
    client.set(schoolName, value, redis.print);
};

//display school value
function displaySchoolValue(schoolName) {
    client.get(schoolName, (error, reply) => {
    if (error) {
        console.log(error);
    } else {
        console.log(reply);
    }
    });
};

//calls
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
