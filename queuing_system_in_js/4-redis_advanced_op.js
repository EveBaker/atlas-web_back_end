const redis = require('redis');
const client = redis.createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err}`);
});

const addFieldsToHash = () => {
  const fieldsToAdd = [
    ['Portland', '50'],
    ['Seattle', '80'],
    ['New York', '20'],
    ['Bogota', '20'],
    ['Cali', '40'],
    ['Paris', '2'],
  ];

  fieldsToAdd.forEach(([city, value], index) => {
    client.hset('HolbertonSchools', city, value, redis.print);
    if (index === fieldsToAdd.length - 1) {
      client.hgetall('HolbertonSchools', (err, result) => {
        if (err) {
          console.error(err);
          return;
        }
        console.log(result);
        client.quit();
      });
    }
  });
};

client.del('HolbertonSchools', addFieldsToHash);