const fs = require('fs');

function countStudents(path) {
try {
    //readfile
    const data = fs.readFileSync(path, 'utf8');

    //splits into lines
    const lines = data.split('\n').filter(line => line !== '');

    //remove header
    lines.shift();

    const students = lines.map(line => {
        const [firstName, , field] = line.split(',');
        return { firstName, field};
    });

    const count = students.length;
    console.log(`Number of students: ${count}`);

    // count by field
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