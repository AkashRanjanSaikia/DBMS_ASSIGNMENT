# Natural Language to SQL Query Generator

**Submitted By:** Akash Ranjan Saikia <br>
**Roll Number:** 230710007003
#

This project demonstrates how to convert **Natural Language Queries (NLQ)** into executable **SQL queries** using Google's Gemini API.

---


## 1. Files Overview

| File | Description |
|------|-------------|
| `nlq_generator.py` | Core engine containing the `generate_sql_with_gemini()` function. Handles prompt creation, API call, and response cleaning. |
| `local_cli.py` | Interactive command-line tool. Allows users to input their own database schema and ask natural language questions in real time. |
| `test_queries.py` | Script to run predefined test queries (V1–V10 style) against a sample schema. Useful for assignments and batch testing. |

---

## 2. Setup Instructions

### Step 1: Install Dependencies
```bash
pip install google-generativeai python-dotenv
```

### Step 2: Set Up API Key
Add the gemini API key on the `.env` file :
```bash
GEMINI_API_KEY="your_api_key_here"
```

---

## 3. How to Use

### Option A: Interactive CLI
Run the following command:
```bash
python local_cli.py
```

Steps:
1. Enter your database schema line by line (using `CREATE TABLE ...` statements).  
2. Type `done` when schema input is complete.  
3. Ask natural language questions.  
4. The program will output the corresponding SQL queries.  
5. Type `exit` or `quit` to stop.  

---

### Option B: Test Predefined Queries
Run:
```bash
python test_queries.py
```

This will:
- Load a sample schema (Students, Courses, Enrollments tables).  
- Execute several test queries (e.g., list student names, find by age, join tables).  
- Print the generated SQL for each query.  

---

## 4. Notes
- Ensure `.env` file is present with a valid `GEMINI_API_KEY`.  
- The model used: **Gemini 2.5 Flash**.  
- `nlq_generator.py` can be imported into other projects as a reusable function.  

---
