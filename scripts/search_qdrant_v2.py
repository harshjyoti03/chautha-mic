import os

from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer

from qdrant_client import QdrantClient

load_dotenv()

client = QdrantClient(
    url=os.getenv("QDRANT_URL"),
    api_key=os.getenv("QDRANT_API_KEY")
)

print("Loading model...")

model = SentenceTransformer(
    "intfloat/multilingual-e5-base"
)

print("Ready!")

while True:

    query = input("\nSearch > ")

    if query.lower() == "exit":
        break

    query_vector = model.encode(
        "query: " + query,
        normalize_embeddings=True
    ).tolist()

    results = client.query_points(
        collection_name="teen_taal_chunks",
        query=query_vector,
        limit=10
    )

    print("\n=====================\n")

    for i, point in enumerate(
        results.points,
        start=1
    ):

        payload = point.payload

        print(
            f"{i}. "
            f"{payload['episode_id']} "
            f"({point.score:.4f})"
        )

        print(payload["title"])

        print()