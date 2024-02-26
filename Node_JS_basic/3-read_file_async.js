const fs = require('fs').promises;

function countStudents(path) {
  return fs.readFile(path, 'utf8')
    .then((data) => {
      const lines = data.split('\n').filter((line) => line !== '');
      // Remove the header
      lines.shift();

      const students = lines.map((line) => {
        const [firstName, , field] = line.split(',');
        return { firstName, field };
      });

      const count = students.length;
      console.log(`Number of students: ${count}`);

      // Count students by field
      const fields = {};
      students.forEach((student) => {
        if (!fields[student.field]) {
          fields[student.field] = [];
        }
        fields[student.field].push(student.firstName);
      });

      Object.keys(fields).forEach((field) => {
        console.log(`Number of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}`);
      });
    })
    .catch(() => {
      throw new Error('Cannot load the database');
    });
}

module.exports = countStudents;
