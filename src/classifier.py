def classify_document(text):

    text = text.lower()

    if "प्रश्न" in text:
        return "exam"

    if "chapter" in text:
        return "chapter"

    if "unit" in text:
        return "chapter"

    if "assignment" in text:
        return "assignment"

    return "notes"