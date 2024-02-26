const { readDatabase } = require('../utils.js');

class StudentsController {
  static async getAllStudents(req, res) {
    try {
      const data = await readDatabase();
      let response = 'This is the list of our students\n';
      const fields = Object.keys(data).sort();
      fields.forEach((field) => {
        const studentList = data[field].join(', ');
        response += `Number of students in ${field}: ${data[field].length}. List: ${studentList}\n`;
      });
      res.status(200).send(response.trim());
    } catch (error) {
      res.status(500).send('Cannot load the database');
    }
  }

  static async getAllStudentsByMajor(req, res) {
    const { major } = req.query;
    if (!['CS', 'SWE'].includes(major)) {
      return res.status(500).send('Major parameter must be CS or SWE');
    }

    try {
      const data = await readDatabase();
      if (!data[major]) {
        return res.status(500).send('Cannot load the database');
      }
      const studentList = data[major].join(', ');
      res.status(200).send(`List: ${studentList}`);
    } catch (error) {
      res.status(500).send('Cannot load the database');
    }
    return undefined;
  }
}

module.exports = StudentsController;
