import re

def extract_topic(text):

    first_part = text[:2000]

    lines = first_part.split("\n")

    for line in lines:

        line = line.strip()

        if not line:
            continue

        if len(line) < 5:
            continue

        if len(line) > 120:
            continue

        if "table of contents" in line.lower():
            continue

        if line.lower().startswith("chapter"):
            return line

    for line in lines:

        line = line.strip()

        if (
            len(line) > 10
            and len(line) < 80
        ):
            return line

    return "Unknown Topic"