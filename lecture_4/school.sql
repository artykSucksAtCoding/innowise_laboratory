/*
    Script for the school database.
    Contains two tables: students and grades.
    1. Create tables.
    2. Insert sample data.
    3. Run validation queries.
*/

/* ---------- Create the students table ---------- */
CREATE TABLE If NOT EXISTS students
(
    id INTEGER PRIMARY KEY AUTOINCREMENT, -- Unique student identifier
    full_name TEXT NOT NULL,              -- Student's full name
	birth_year INTEGER                    -- Student's year of birth
);

/* ---------- Create the grades table ---------- */
CREATE TABLE IF NOT EXISTS grades
(
    id INTEGER PRIMARY KEY AUTOINCREMENT, -- Unique grade identifier
    student_id INTEGER,                   -- Foreign key referencing student
	subject TEXT NOT NULL,                -- Subject name
	grade INTEGER,                        -- Grade value
	FOREIGN KEY (student_id)  REFERENCES students (id) -- Link to student table
);

/* ---------- Insert sample students ---------- */
INSERT INTO students (full_name, birth_year)
VALUES
    ('Alice Johnson', 2005),
    ('Brian Smith', 2004),
    ('Carla Reyes', 2006),
    ('Daniel Kim', 2005),
    ('Eva Thompson', 2003),
    ('Felix Nguyen', 2007),
    ('Grace Patel', 2005),
    ('Henry Lopez', 2004),
    ('Isabella Martinez', 2006);

/* ---------- Insert sample grades ---------- */
INSERT INTO grades (student_id, subject, grade)
VALUES
	(1, 'Math', 88),
	(1, 'English', 92),
	(1, 'Science', 85),
	(2, 'Math', 75),
	(2, 'History', 83),
	(2, 'English', 79),
	(3, 'Science', 95),
	(3, 'Math', 91),
	(3, 'Art', 89),
	(4, 'Math', 84),
	(4, 'Science', 88),
	(4, 'Physical Education', 93),
	(5, 'English', 90),
	(5, 'History', 85),
	(5, 'Math', 88),
	(6, 'Science', 72),
	(6, 'Math', 78),
	(6, 'English', 81),
	(7, 'Art', 94),
	(7, 'Science', 87),
	(7, 'Math', 90),
	(8, 'History', 77),
	(8, 'Math', 83),
	(8, 'Science', 80),
	(9, 'English', 96),
	(9, 'Math', 89),
	(9, 'Art', 92);

-- All grades for Alice Johnson
SELECT full_name, grade
FROM grades
JOIN students on students.id = student_id
WHERE full_name = "Alice Johnson";

-- Average grade for each student
SELECT students.id, students.full_name, AVG(grades.grade) AS avg_grade
FROM students
JOIN grades ON students.id = grades.student_id
GROUP BY students.id, students.full_name;

-- Students born after 2004
SELECT full_name, birth_year FROM students
WHERE birth_year > 2004;

-- Average grade per subject
SELECT grades.subject, AVG(grades.grade) AS avg_grade
FROM grades
GROUP BY grades.subject;

-- Top 3 students by average grade
SELECT students.id, students.full_name, AVG(grades.grade) AS avg_grade
FROM students
JOIN grades ON students.id = grades.student_id
GROUP BY students.id, students.full_name
ORDER BY avg_grade DESC
LIMIT 3;

-- Students having minimal grade less than 80
SELECT students.id, students.full_name, MIN(grades.grade) AS min_grade
FROM students
JOIN grades on students.id = grades.student_id
GROUP BY students.full_name, student_id
HAVING min_grade < 80;



