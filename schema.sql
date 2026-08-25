CREATE TABLE Course (
CourseID INT PRIMARY KEY,
CourseName VARCHAR(50),
Credits INT
);
CREATE TABLE Enrollment (
EnrollmentID INT PRIMARY KEY,
StudentID INT,
CourseID INT
);
INSERT INTO Course VALUES
(201, 'Database System', 4),
(202, 'Data Structures', 3),
(203, 'Mathematics', 4);
INSERT INTO Enrollment VALUES
(1, 1001, 201),
(2, 1001, 202),
(3, 1002, 203),
(4, 1003, 201);
SELECT
Course.CourseID,
Course.CourseName,
Course.Credits,
Enrollment.EnrollmentID,
Enrollment.StudentID
FROM Course
LEFT JOIN Enrollment
ON Course.CourseID = Enrollment.CourseID;

SELECT
Course.CourseID,
Course.CourseName,
Course.Credits,
Enrollment.EnrollmentID,
Enrollment.StudentID
FROM Course
RIGHT JOIN Enrollment
ON Course.CourseID = Enrollment.CourseID
