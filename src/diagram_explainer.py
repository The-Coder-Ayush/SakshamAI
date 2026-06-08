import ollama

MODEL = "llama3.2:1b"


def explain_diagram(
    diagram_name,
    student_level
):

    prompt = f"""
You are an expert teacher.

Diagram:
{diagram_name}

Student Level:
{student_level}

Explain the diagram.

Rules:

- Be scientifically correct
- Use simple language
- Adjust explanation according to student level
- Do not invent labels that are not normally found in the diagram

Format:

📘 DIAGRAM NAME

🌱 WHAT IS IT?

🔍 MAIN PARTS

🧠 MEMORY TRICK

🤔 CHECK YOURSELF

✅ ANSWER
"""

    response = ollama.chat(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]