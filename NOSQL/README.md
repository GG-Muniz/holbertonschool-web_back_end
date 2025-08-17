# NoSQL

MongoDB and PyMongo tasks.

- MongoDB 4.4
- Python 3.9, PyMongo 4.8.0
- All files end with a new line
- Mongo shell scripts start with `// my comment`
- Python scripts start with `#!/usr/bin/env python3`
- Code style: pycodestyle 2.5.*

## Files
- `0-list_databases`: list all databases
- `1-use_or_create_database`: use/create `my_db`
- `2-insert`: insert document `{ name: "Holberton school" }` into `school`
- `3-all`: list all documents in `school`
- `4-match`: list documents in `school` with `name="Holberton school"`
- `5-count`: count documents in `school`
- `6-update`: add `address: "972 Mission street"` to docs with that name
- `7-delete`: delete documents with `name="Holberton school"`
- `8-all.py`: list all documents in a collection
- `9-insert_school.py`: insert document with kwargs and return `_id`
- `10-update_topics.py`: update topics by school name
- `11-schools_by_topic.py`: find schools by topic
- `12-log_stats.py`: print Nginx logs stats 