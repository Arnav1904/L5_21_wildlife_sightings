# Reflection

Note: The lab handout was not in the repository. Check that these headings match its four reflection questions.

## 1. Which issues were most important to fix, and why?

SQL injection was the most serious issue because input could change the database query. The shared default dictionary and empty-table crash could also cause incorrect results or stop the program. I used SQL placeholders, created a fresh dictionary when needed, and handled empty results.

## 2. How did Pylint, Flake8, and Bandit help?

Pylint checks code quality and common mistakes. Flake8 checks style and formatting. Bandit looks for common security risks. Using all three checks more areas than using one tool alone.

## 3. Why is it not enough to remove warnings?

A clean report does not prove that the program is correct. I also need to test normal input and edge cases, such as an empty database, invalid counts, and text that looks like SQL.

## 4. What did you learn?

Static analysis helps find problems early. The useful process is to review each finding, fix the cause, run the tools again, and test that the program still works.
