from sentence_transformers import (
    SentenceTransformer
)

from chunker import chunk_text
from embedder import create_embeddings

from vector_store import (
    build_index,
    search_index
)

MODEL = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


def retrieve_context(
    text,
    query,
    top_k=3
):

    chunks = chunk_text(text)

    embeddings = create_embeddings(
        chunks
    )

    index = build_index(
        embeddings
    )

    query_embedding = MODEL.encode(
        query,
        convert_to_numpy=True
    )

    indices = search_index(
        index,
        query_embedding,
        top_k
    )

    retrieved_chunks = []

    for idx in indices:

        if idx < len(chunks):

            retrieved_chunks.append(
                chunks[idx]
            )

    return "\n\n".join(
        retrieved_chunks
    )