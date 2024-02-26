const fs = require('fs');

function countStudents(path) {
    let content;
}

try {
    content = fs.readFileSync(path, 'utf8');
    
} catch (err) {
    throw new Error('Cannot load the database');
}

//split content, filter empty lines
const lines = content.split('\n').filter(line => line);

//number of students
const NUMBER_OF_STUDENTS = lines.length - 1;
console.log(`Number of students: ${NUMBER_OF_STUDENTS}`);

//initalize
const fields = {};

for (let i = 1; i < lines.length; i++) {
    const [name, , , field] = lines[i].split(',');
    if (field) { // Check if field is not undefined
      if (!fields[field]) fields[field] = [];
      fields[field].push(name);
    }
  }

//Itorate student log info
for (const [key, value] of Object.entries(fields)) {
    console.log(`Number of students in ${key}: ${value.length}. List: ${value.join(', ')}`);
  }

module.exports = countStudents;