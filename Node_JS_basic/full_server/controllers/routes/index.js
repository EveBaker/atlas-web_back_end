const express = require('express');

const router = express.Router();
const AppControler = require('../controllers/AppController.js');
const StudentsController = require('../controllers/StudentsController.js');

router.get('/', AppControler.gethomepage);
router.get('/students', StudentsController.getALLStudents);
router.get('/students/:major', StudentsController.getALLStudentsByMajor);

module.exports = router;
