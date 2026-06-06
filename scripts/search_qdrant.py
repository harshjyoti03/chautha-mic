import os

from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer

from qdrant_client import QdrantClient

load_dotenv()

QDRANT_URL = os.getenv("QDRANT_URL")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")

client = QdrantClient(
    url=QDRANT_URL,
    api_key=QDRANT_API_KEY
)

print("Loading model...")

model = SentenceTransformer(
    "BAAI/bge-small-en-v1.5"
)

print("Ready!")

while True:

    query = input("\nSearch > ")

    if query.lower() == "exit":
        break

    query_vector = model.encode(
        query,
        normalize_embeddings=True
    ).tolist()

    results = client.query_points(
        collection_name="teen_taal_chunks",
        query=query_vector,
        limit=5
    )

    print("\n========================\n")

    for i, point in enumerate(results.points, start=1):

        payload = point.payload

        print(f"Result #{i}")
        print(f"Score: {point.score:.4f}")
        print(f"Episode: {payload['episode_id']}")
        print(f"Title: {payload['title']}")
        print()

        preview = payload["text"][:500]

        print(preview)
        print("\n------------------------\n")