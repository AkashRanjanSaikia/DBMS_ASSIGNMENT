# test_queries.py

"""
Test Suite for NLQ-to-SQL Generator.

This script tests the `generate_sql_with_gemini` function by providing
a predefined schema and a set of natural language queries (NLQs).
It prints the generated SQL queries for verification.
"""

from nlq_generator import generate_sql_with_gemini


# -----------------------------
# 1. Define the Database Schema
# -----------------------------
SCHEMA = """
CREATE TABLE students (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER,
    grade TEXT,
    marks INTEGER,
    date_of_admission DATE
);

CREATE TABLE courses (
    course_id INTEGER PRIMARY KEY,
    course_name TEXT NOT NULL,
    student_id INTEGER,
    FOREIGN KEY (student_id) REFERENCES students (id)
);
"""


# -----------------------------
# 2. Define Test Cases (V1–V10)
# -----------------------------
TEST_CASES = [
    # V1: Basic Rule-Based Query
    "Show all students with marks > 80",

    # V2: Multi-Condition Query
    "List students older than 20 and with grade 'A'",

    # V3: Aggregation Query
    "Find the average marks of students",

    # V4: Sorting Query
    "Show students ordered by marks descending",

    # V5: Grouping Query
    "Show average marks by grade",

    # V6: Multi-Table Query (JOIN)
    "Show student names with their course names",

    # V7: Synonym Handling
    "What are the scores for students with a score above 70?",

    # V8: Comparative Query (Subquery)
    "Find students with marks higher than Priya's",

    # V9: Time/Date Query
    "Which students were admitted after 2020",

    # V10: Nested Query
    "Find students with marks greater than the average",
]


# -----------------------------
# 3. Run Tests
# -----------------------------
def run_tests():
    """Run all test cases and print results."""
    print("\n--- DBMS NLQ to SQL Test Suite ---")
    print("Model: Google Gemini 2.5 Flash (via API)")
    print("Schema: Students and Courses tables")
    print("-" * 60)

    for i, nlq in enumerate(TEST_CASES, start=1):
        print(f"TEST {i}")
        print(f"  NLQ: {nlq}")

        # Call the NLQ → SQL generator
        generated_sql = generate_sql_with_gemini(nlq, SCHEMA)

        print(f"  SQL: {generated_sql}")
        print("-" * 60)


# -----------------------------
# 4. Script Entry Point
# -----------------------------
if __name__ == "__main__":
    run_tests()
