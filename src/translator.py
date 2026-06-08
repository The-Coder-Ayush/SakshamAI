import ollama

MODEL = "llama3.2:1b"


def translate_text(text, target_language):

    if target_language == "English":
        return text

    prompt = f"""
Translate the educational content below into {target_language}.

IMPORTANT:
- Return ONLY the translated content.
- Do NOT explain.
- Do NOT add notes.
- Do NOT add headings.
- Do NOT repeat instructions.
- Do NOT add translator comments.
- Preserve formatting.

CONTENT START

{text}

CONTENT END
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