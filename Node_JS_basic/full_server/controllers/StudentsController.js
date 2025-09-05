import readDatabase from '../utils';

class StudentsController {
  static async getAllStudents(req, res) {
    const databasePath = process.argv[2];
    try {
      const data = await readDatabase(databasePath);
      const fields = Object.keys(data)
        .sort((a, b) => a.toLowerCase().localeCompare(b.toLowerCase()));
      const lines = ['This is the list of our students'];
      fields.forEach((field) => {
        const list = data[field] || [];
        lines.push(`Number of students in ${field}: ${list.length}. List: ${list.join(', ')}`);
      });
      res.status(200).send(lines.join('\n'));
    } catch (e) {
      res.status(500).send('Cannot load the database');
    }
  }

  static async getAllStudentsByMajor(req, res) {
    const { major } = req.params;
    if (major !== 'CS' && major !== 'SWE') {
      res.status(500).send('Major parameter must be CS or SWE');
      return;
    }
    const databasePath = process.argv[2];
    try {
      const data = await readDatabase(databasePath);
      const list = data[major] || [];
      res.status(200).send(`List: ${list.join(', ')}`);
    } catch (e) {
      res.status(500).send('Cannot load the database');
    }
  }
}

export default StudentsController;
