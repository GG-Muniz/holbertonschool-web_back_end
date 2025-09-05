const http = require('http');
const fs = require('fs');

function buildStudentsReport(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }
      const lines = data.split('\n').filter((line) => line.trim().length > 0);
      if (lines.length <= 1) {
        resolve('Number of students: 0');
        return;
      }
      const students = lines.slice(1);
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

      const total = students.length;
      const linesOut = [`Number of students: ${total}`];
      Object.keys(fieldGroups).forEach((field) => {
        const list = fieldGroups[field];
        linesOut.push(`Number of students in ${field}: ${list.length}. List: ${list.join(', ')}`);
      });
      resolve(linesOut.join('\n'));
    });
  });
}

const databasePath = process.argv[2];

const app = http.createServer((req, res) => {
  res.setHeader('Content-Type', 'text/plain');
  if (req.url === '/') {
    res.statusCode = 200;
    res.end('Hello Holberton School!');
  } else if (req.url === '/students') {
    res.statusCode = 200;
    const header = 'This is the list of our students';
    buildStudentsReport(databasePath)
      .then((report) => {
        res.end(`${header}\n${report}`);
      })
      .catch(() => {
        res.end(`${header}\nCannot load the database`);
      });
  } else {
    res.statusCode = 404;
    res.end();
  }
});

app.listen(1245);

module.exports = app;
