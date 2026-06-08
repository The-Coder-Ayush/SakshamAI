from sentence_transformers import (
    SentenceTransformer
)

MODEL = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


def create_embeddings(chunks):

    embeddings = MODEL.encode(
        chunks,
        convert_to_numpy=True
    )

    return embeddings