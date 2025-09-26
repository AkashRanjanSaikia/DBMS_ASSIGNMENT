# nlq_generator.py

"""
Natural Language to SQL Generator using Gemini API.

This script defines a function that converts a natural language query 
into an SQL query based on a given schema using Google's Gemini model.
"""

import os
import textwrap
import google.generativeai as genai
from dotenv import load_dotenv


# -----------------------------
# 1. Load Environment Variables
# -----------------------------
load_dotenv()

try:
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY environment variable not set.")

    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-2.5-flash")

except Exception as e:
    print(f"[ERROR] Could not configure Gemini API. Details: {e}")
    model = None


# -----------------------------
# 2. Core Function
# -----------------------------
def generate_sql_with_gemini(natural_language_query: str, create_table_statements: str) -> str:
    """
    Generates an SQL query using the Gemini model given a natural language question and schema.

    Args:
        natural_language_query (str): The user’s question in plain English.
        create_table_statements (str): The SQL CREATE TABLE statements (schema).

    Returns:
        str: The generated SQL query or an error message.
    """
    if model is None:
        return "Model not loaded. Cannot generate SQL."

    # Prompt for Gemini
    prompt = textwrap.dedent(f"""
        Given the following SQL tables, your job is to write a single, clean SQL query given a user's request.
        DO NOT include any explanation or extra text, only the SQL query.

        ### CREATE TABLE statements (Schema):
        {create_table_statements}

        ### User's question:
        {natural_language_query}

        ### SQL Query:
    """).strip()

    try:
        response = model.generate_content(prompt)
        sql_query = (
            response.text.strip()
            .replace("```sql", "")
            .replace("```", "")
            .strip()
        )
        return sql_query

    except Exception as e:
        return f"API Error: {e}"


# -----------------------------
# 3. Run as Script
# -----------------------------
if __name__ == "__main__":
    print("This file contains the core function.")
    print("Run 'test_queries.py' to test SQL generation.")
