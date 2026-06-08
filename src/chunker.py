def chunk_text(
    text,
    chunk_size=120,
    overlap=30
):

    words = text.split()

    chunks = []

    start = 0

    while start < len(words):

        end = start + chunk_size

        chunk = " ".join(
            words[start:end]
        )

        chunks.append(chunk)

        start += (
            chunk_size - overlap
        )

    print(
        "\nTOTAL CHUNKS:",
        len(chunks)
    )

    return chunks