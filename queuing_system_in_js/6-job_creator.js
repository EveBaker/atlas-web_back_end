const kue = require('kue');
const queue = kue.createQueue();

const jobData = {
    phoneNumber: '1234567890',
    message: 'Your code is 1234',
};

const job = queue.create('push_notification_code', jobData).save((err) => {
    if (!err) console.log(`Notification job created: ${job.id}`);
});

job.on('complete', () => console.log('Notification job completed'))
   .on('failed', (err) => console.log('Notification job failed', err))