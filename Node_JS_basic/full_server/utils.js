const fs = require('fs').promises;

const readDatabase = (filePath) => fs.readFile(filePath, { encoding: 'utf8' })
  .then((data) => {
    const lines = data.split('\n').filter(Boolean);
    const students = {};
    lines.forEach((line) => {
      const [field, name] = line.split(',');
      if (!students[field]) students[field] = [];
      students[field].push(name);
    });
    return students;
  })
  .catch((error) => {
    throw error;
  });

module.exports = { readDatabase };
