from qdrant_client import QdrantClient
from dotenv import load_dotenv
import os

load_dotenv()

client = QdrantClient(
    url=os.getenv("QDRANT_URL"),
    api_key=os.getenv("QDRANT_API_KEY")
)

points, _ = client.scroll(
    collection_name="teen_taal_chunks",
    limit=5,
    with_payload=True
)

for p in points:

    print("\nID:")
    print(p.id)

    print("\nPAYLOAD:")
    print(p.payload)

    print("=" * 80)