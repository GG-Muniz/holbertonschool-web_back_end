const fs = require('fs');

function countStudents(path) {
  try {
    const data = fs.readFileSync(path, 'utf8');
    const lines = data.split('\n').filter((line) => line.trim().length > 0);
    if (lines.length <= 1) {
      console.log('Number of students: 0');
      return;
    }
    const students = lines.slice(1);
    const total = students.length;
    console.log(`Number of students: ${total}`);

    const fieldGroups = {};
    students.forEach((line) => {
      const parts = line.split(',');
      if (parts.length >= 4) {
        const firstname = parts[0].trim();
        const field = parts[3].trim();
        if (!fieldGroups[field]) fieldGroups[field] = [];
        fieldGroups[field].push(firstname);
      }
    });

    Object.keys(fieldGroups).forEach((field) => {
      const list = fieldGroups[field];
      console.log(`Number of students in ${field}: ${list.length}. List: ${list.join(', ')}`);
    });
  } catch (err) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
