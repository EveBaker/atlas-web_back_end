const fs = require('fs');

function countStudents(path) {
  try {
    // Read the file
    const data = fs.readFileSync(path, 'utf8');

    // Split the file 
    const lines = data.split('\n').filter(line => line !== '');

    // Remove the header
    lines.shift();

    const students = lines.map(line => {
      const [firstName, , field] = line.split(',');
      return { firstName, field };
    });

    const count = students.length;
    console.log(`Number of students: ${count}`);

    // Count students by field
    const fields = {};
    students.forEach(student => {
      if (!fields[student.field]) {
        fields[student.field] = [];
      }
      fields[student.field].push(student.firstName);
    });

    for (const field in fields) {
      console.log(`Number of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}`);
    }
  } catch (err) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;