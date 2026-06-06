import os
import json

from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer
from qdrant_client import QdrantClient

load_dotenv()

INDEX_FILE = (
    r"E:\POLO\Chautha Mic\metadata\chunk_index.json"
)

with open(
    INDEX_FILE,
    "r",
    encoding="utf-8"
) as f:
    chunk_index = json.load(f)

client = QdrantClient(
    url=os.getenv("QDRANT_URL"),
    api_key=os.getenv("QDRANT_API_KEY")
)

print("Loading model...")

model = SentenceTransformer(
    "intfloat/multilingual-e5-base"
)

print("Ready")

while True:

    query = input("\nSearch > ")

    if query.lower() == "exit":
        break

    vector = model.encode(
        "query: " + query,
        normalize_embeddings=True
    ).tolist()

    results = client.query_points(
        collection_name="teen_taal_chunks",
        query=vector,
        limit=10
    )

    print("\n====================\n")

    for i, point in enumerate(
        results.points,
        start=1
    ):

        payload = point.payload

        chunk_id = payload["chunk_id"]

        meta = chunk_index[chunk_id]

        print(
            f"{i}. "
            f"{payload['episode_id']} "
            f"({point.score:.4f})"
        )

        print(
            payload["title"]
        )

        print(
            meta["path"]
        )

        print()