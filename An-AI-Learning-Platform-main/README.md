# Quest: An AI Learning Platform for C and Java

A gamified website that teaches **C** and **Java** from zero, in simple words, so that even a 15-year-old can learn.
Built with Python, Django, SQLite, HTML, CSS and JavaScript.

## What is inside
- **30 levels for C** and **30 levels for Java**. Each level has a simple lesson, an example, a challenge, a hint, a solution and a quiz.
- **7 real mini projects per language** (levels marked "Mini Project"):

| Project | C level | Java level |
|---|---|---|
| Pocket Money Tracker | 6 | 5 |
| Simple Calculator | 10 | 9 |
| Times Table and Guessing Game | 15 | 13 |
| Marks Report Card | 20 | 17 |
| Student Record Keeper | 24 | 21 |
| ATM Machine / Bank Account | 29 | 28 |
| Final Capstone: To-Do List Manager | 30 | 30 |

- **Voice Teacher**: an ON/OFF switch on every level that reads the lesson aloud (uses the browser's built-in voice, free, no API key). Pause, stop, speed control, and a speaker icon for each section. The choice is remembered.
- **Practice box** that checks the student's code ideas (ignoring comments) and a **Show Solution** button.
- **AI helper**, XP, ranks, unlock-next-level system and profile page.

## Run it
```bash
pip install django
python manage.py migrate
python manage.py seed_courses --reset-progress
python manage.py runserver
```
Open http://127.0.0.1:8000/ (demo login: `developer` / `password123`, or register a new account).

`--reset-progress` clears old saved progress. Use it once when moving from the old 20 levels to the new 30.

## Check the lesson content
```bash
python validate_curriculum.py        # needs gcc (for C) and Java 11+ (for Java)
```
It compiles every solution, runs it, and compares the output with the expected output shown on the website.

## Run the website tests
```bash
python manage.py test
```

## Where to edit lessons
All lessons live in `core/curriculum/`:
`c_part1.py` (C levels 1-15), `c_part2.py` (16-30), `java_part1.py` (Java 1-15), `java_part2.py` (16-30).
After editing, run `python manage.py seed_courses` again.

## Voice feature files
`static/js/voice.js` (logic) + the `voice-panel` block in `templates/course/level_detail.html` + styles at the end of `static/css/style.css`.
Works in Chrome, Edge and Safari.
