import os

from dotenv import load_dotenv
from qdrant_client import QdrantClient

from backend.models import embedding_model

load_dotenv()

client = QdrantClient(
    url=os.getenv("QDRANT_URL"),
    api_key=os.getenv("QDRANT_API_KEY")
)


def search_chunks(
    query,
    limit=10
):

    query_vector = embedding_model.encode(
        "query: " + query,
        normalize_embeddings=True
    ).tolist()

    results = client.query_points(
        collection_name="teen_taal_chunks",
        query=query_vector,
        limit=limit
    )

    chunks = []

    for point in results.points:

        chunks.append({

            "score":
                point.score,

            "chunk_id":
                point.payload["chunk_id"],

            "episode_id":
                point.payload["episode_id"],

            "title":
                point.payload["title"]
        })

    return chunks