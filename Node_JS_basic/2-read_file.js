const fs = require('fs');

function countStudents(path) {
  try {
    if (!fs.existsSync(path)) {
      throw new Error('Cannot load the database');
    }

    const data = fs.readFileSync(path, 'utf8');
    const lines = data.trim().split('\n').slice(1);

    const studentsByField = {};
    let totalStudents = 0;

    lines.forEach((line) => {
      const [firstName, , field] = line.split(',');
      if (!studentsByField[field]) studentsByField[field] = [];
      studentsByField[field].push(firstName);
      totalStudents++;
    });

    console.log(`Number of students: ${totalStudents}`);

    Object.entries(studentsByField).forEach(([field, names]) => {
      console.log(`Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`);
    });
  } catch (err) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;