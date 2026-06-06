import os

from dotenv import load_dotenv

from qdrant_client import QdrantClient
from qdrant_client.models import (
    Distance,
    VectorParams
)

load_dotenv()

client = QdrantClient(
    url=os.getenv("QDRANT_URL"),
    api_key=os.getenv("QDRANT_API_KEY")
)

COLLECTION_NAME = (
    "teen_taal_chunks"
)

if client.collection_exists(
    COLLECTION_NAME
):
    client.delete_collection(
        COLLECTION_NAME
    )

client.create_collection(
    collection_name=COLLECTION_NAME,

    vectors_config=VectorParams(
        size=768,
        distance=Distance.COSINE
    )
)

print("Collection Created")