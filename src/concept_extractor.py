import ollama
import re

MODEL = "llama3.2:1b"


def extract_concepts(text):

    sample = (
    text[:4000]
    + "\n"
    + text[len(text)//2 : len(text)//2 + 4000]
    + "\n"
    + text[-4000:]
)

    text = sample

    prompt = f"""
You are an educational concept extractor.

Chapter:

{text}

Extract ONLY concepts directly mentioned in the chapter.

Rules:

- Do not infer concepts.
- Do not add related topics.
- Do not use outside knowledge.
- Use only words present in the text.
- Return exactly 7 concepts if available.

Rules:
- Return only concept names
- One concept per line
- No numbering
- No explanations
- No sentences
- Maximum 4 words per concept

Example:

Photosynthesis
Sunlight
Water
Carbon Dioxide
Chlorophyll
Glucose
Oxygen
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

    output = response["message"]["content"]

    concepts = []

    for line in output.split("\n"):

        line = re.sub(
            r"^[0-9\.\-\*\)\s]+",
            "",
            line.strip()
        )

        if not line:
            continue

        if len(line.split()) > 4:
            continue

        if line not in concepts:
            concepts.append(line)

    words = []

    for word in text.split():

     word = word.strip(",.:;()")

     if len(word) > 5:
           words.append(word)

    if len(concepts) == 0:

      concepts = list(
        dict.fromkeys(words)
     )

    return concepts[:7]


def extract_difficult_words(concepts):

    difficult = []

    for concept in concepts:

        if len(concept) > 6:
            difficult.append(concept)

    return difficult[:4]