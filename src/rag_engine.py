from chunker import chunk_text

from embedder import (
    create_embeddings,
    MODEL
)

from vector_store import (
    build_index,
    search_index
)


class RAGEngine:

    def __init__(self, document_text):

        self.document_text = document_text

        self.chunks = chunk_text(
            document_text
        )
        print("\nFIRST CHUNK:")
        print(self.chunks[0][:1000])

        self.embeddings = (
            create_embeddings(
                self.chunks
            )
        )

        self.index = build_index(
            self.embeddings
        )

    def retrieve(
        self,
        query,
        top_k=5
    ):

        query_embedding = MODEL.encode(
            query,
            convert_to_numpy=True
        )

        distances, indices = search_index(
            self.index,
            query_embedding,
            top_k
        )

        results = []

        for idx in indices:

            if idx < len(self.chunks):

                results.append(
                    self.chunks[idx]
                )

        print("\nDEBUG DISTANCES:")
        print(distances)

        return {
    "context": "\n\n".join(results),
    "distances": distances.tolist()
     }