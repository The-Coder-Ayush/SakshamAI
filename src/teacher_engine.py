import ollama
from confidence_scorer import (
    calculate_confidence,
    confidence_label
)

MODEL = "llama3.2:1b"


def run_prompt(prompt):

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


def generate_explanation(
    topic,
    concepts,
    rag,
    student_level,
    language
):

    query = topic + " " + " ".join(concepts)

    retrieval = rag.retrieve(
    query,
    top_k=5
)

    context = retrieval["context"]
    distances = retrieval["distances"]
    
    confidence_score = calculate_confidence(
       distances
     )

    confidence_level = confidence_label(
       confidence_score
    )

    level_rules = {

    "Class 6":
    """
    Explain like a primary school teacher.
    Use very easy words.
    Use short sentences.
    Use examples from daily life.
    Avoid scientific jargon.
    """,

    "Class 7":
    """
    Explain like a middle school teacher.
    Use simple language.
    Introduce basic scientific terms.
    Give relatable examples.
    """,

    "Class 8":
    """
    Explain with moderate detail.
    Introduce scientific reasoning.
    Explain cause and effect.
    Use educational examples.
    """,

    "Class 9":
    """
    Use proper scientific explanations.
    Explain mechanisms and processes.
    Include real-world applications.
    Use subject terminology.
    """,

    "Class 10":
    """
    Use board-exam level explanations.
    Explain concepts in depth.
    Include scientific reasoning.
    Include practical applications.
    Include exam-relevant understanding.
    """
}

    prompt = f"""
IMPORTANT OUTPUT RULE:

The entire response MUST be in {language}.
Hindi means Hindi language.
English means English language.

Never switch language in the middle.
Never mix Hindi and English paragraphs.

English = English only.
Hindi = Hindi only.

Never mix languages.

You are an expert teacher.

TOPIC:
{topic}

IMPORTANT:

The retrieved context may be much harder
than the student's level.

Rewrite EVERYTHING for {student_level}.

Do NOT copy academic language.

If a term is difficult:
1. Explain it simply.
2. Then give the scientific name.

The final answer must match
the student's class level,
not the document level.

RETRIEVED DOCUMENT CONTENT:

{context}

IMPORTANT OUTPUT RULE:

The entire response MUST be in {language}.

If language is English:
- Use ONLY English.
- Do NOT use Hindi.
- Do NOT mix languages.
- All headings, explanations, examples and notes must be English.

If language is Hindi:

- Write simple school-level Hindi.
- Keep scientific terms in English if translation is difficult.

Examples:

Digestive System (पाचन तंत्र)
Liver (यकृत)
Pancreas (अग्न्याशय)
Stomach (आमाशय)

NEVER invent Hindi words.
NEVER create fake scientific terminology.
NEVER translate technical terms incorrectly.

If unsure, keep the original English scientific term.

Use natural Hindi that a school student can understand.

Violation of language rules is not allowed.

STUDENT LEVEL:
{student_level}

RULES:
{level_rules.get(student_level)}

DOCUMENT PRIORITY RULES:

1. Use the uploaded document as the PRIMARY source.
2. Explain all important points present in the document.
3. Do not contradict the document.
4. Additional educational information is allowed.
5. Clearly separate additional information.
6. Keep explanations suitable for the student's level.
7. If the document is short, expand the explanation using educational knowledge.

Explain using ONLY the uploaded document.

Format:

📘 What is it?

🔍 Key Points From Document

🌟 Importance

📝 Example

📚 Additional Information
(Optional if useful)



⚠ Source:
Document + Educational Knowledge

If example is not present in context,
say:

"Example not available in uploaded document."

Return only explanation.
"""

    return {
    "explanation": run_prompt(prompt),
    "confidence_score": confidence_score,
    "confidence_level": confidence_level
}


def generate_memory_trick(
    topic,
    concepts,
    rag,
    language
):

    query = topic + " " + " ".join(concepts)

    retrieval = rag.retrieve(
      query,
      top_k=5
    )
    context = retrieval["context"][:3000]
    prompt = f"""
TOPIC:
{topic}

CONTEXT:
{context}

LANGUAGE:
{language}

Create a memory trick specifically for:

TOPIC: {topic}

CONCEPTS:
{", ".join(concepts)}

Rules:

- Must use the actual concepts.
- Must help remember the process.
- Must be related to the topic.
- Do not use generic memory tricks.
- Maximum 12 words.

Example:

Water Cycle:
"Evaporate, Condense, Rain, Collect — Repeat Again"

Return only the memory trick.

Photosynthesis:
"Plants Prepare Food Using Sunlight"

Return ONLY the memory trick.

Do NOT explain.
Do NOT repeat instructions.
Do NOT repeat rules.
Do NOT repeat topic.
Do NOT return examples.

Output must be exactly one sentence.

OUTPUT LANGUAGE:

If English:
Return English only.

If Hindi:
Return Hindi only.

Use ONLY concepts from:
{", ".join(concepts)}

Never use concepts from other topics.
Never create unrelated memory tricks.

Maximum one sentence.
"""

    return run_prompt(prompt)


def generate_question(
    topic,
    concepts,
    rag,
    level,
    language
):

    query = topic + " " + " ".join(concepts)

    retrieval = rag.retrieve(
        query,
        top_k=5
     )
    context = retrieval["context"]
    prompt = f"""
TOPIC:
{topic}

CONTEXT:
{context}

STUDENT LEVEL:
{level}

LANGUAGE:
{language}

Create one conceptual question.

No MCQ.
No True/False.
One question only.

Use the requested language.
"""

    return run_prompt(prompt)


def generate_answer(
    topic,
    concepts,
    rag,
    question,
    language
):

    query = topic + " " + " ".join(concepts)

    retrieval = rag.retrieve(
        query,
        top_k=5
    )
    context = retrieval["context"]
    prompt = f"""
CONTEXT:
{context}

QUESTION:
{question}

LANGUAGE:
{language}

Answer in 2-3 sentences.

Use ONLY the context.
Use the requested language.
"""

    return run_prompt(prompt)


def generate_dictionary(
    difficult_words,
    language
):

    result = []

    for word in difficult_words:

        prompt = f"""
TERM:
{word}

LANGUAGE:
{language}

Explain the term.

Rules:
- One sentence only
- Easy language
- Maximum 15 words

If Hindi:
Keep scientific names transliterated.

Return only the definition.
"""

        meaning = run_prompt(prompt)

        meaning = (
            meaning
            .replace("\n", " ")
            .strip()
        )

        result.append(
            f"{word}: {meaning}"
        )

    return "\n".join(result)