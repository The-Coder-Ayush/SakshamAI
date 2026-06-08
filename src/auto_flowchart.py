def generate_auto_flowchart(concepts):

    cleaned = []

    for concept in concepts:

        concept = concept.strip()

        if concept and concept not in cleaned:
            cleaned.append(concept)

    if len(cleaned) == 0:
        return "Flowchart unavailable"

    return "\n↓\n".join(cleaned[:5])