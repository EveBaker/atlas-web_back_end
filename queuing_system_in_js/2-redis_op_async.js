//import redis
import redis from 'redis';
const { promisify } = require('util');

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
const setNewSchool = (schoolName, value) => {
  client.set(schoolName, value, redis.print);
};

//display school value
const getAsync = promisify(client.get).bind(client);
const displaySchoolValue = async (schoolName) => {
  try {
    const value = await getAsync(schoolName);
    console.log(value);
  } catch (err) {
    console.error(err);
  }
};


//calls
(async () => {
  await displaySchoolValue('Holberton');
  await setNewSchool('HolbertonSanFrancisco', '100');
  await displaySchoolValue('HolbertonSanFrancisco');
})();