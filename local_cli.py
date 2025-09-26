# local_cli.py
from nlq_generator import generate_sql_with_gemini

print("Enter your database schema (CREATE TABLE statements).")
print("Type 'done' when finished.\n")

schema_lines = []
while True:
    line = input()
    if line.lower().strip() == 'done':
        break
    schema_lines.append(line)

schema = "\n".join(schema_lines)

if not schema.strip():
    print("No schema provided. Exiting.")
    exit()

print("\n✅ Schema captured! Now ask your questions (type 'exit' to quit).\n")

while True:
    question = input("Your question: ")
    if question.lower().strip() in ["exit", "quit"]:
        print("Exiting interactive session. Goodbye!")
        break
    if not question.strip():
        continue

    sql = generate_sql_with_gemini(question, schema)
    print("\n➡️ Generated SQL:")
    print(sql, "\n")
    print("-" * 60)
