import fs from 'fs';

export default function readDatabase(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) {
        reject(err);
        return;
      }
      try {
        const lines = data.split('\n').filter((line) => line.trim().length > 0);
        const result = {};
        if (lines.length <= 1) {
          resolve(result);
          return;
        }
        const students = lines.slice(1);
        students.forEach((line) => {
          const parts = line.split(',');
          if (parts.length >= 4) {
            const firstname = parts[0].trim();
            const field = parts[3].trim();
            if (!result[field]) result[field] = [];
            result[field].push(firstname);
          }
        });
        resolve(result);
      } catch (e) {
        reject(e);
      }
    });
  });
} 