import os
import json

from tqdm import tqdm
from dotenv import load_dotenv

from sentence_transformers import SentenceTransformer

from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct

# ---------------------------------------
# CONFIG
# ---------------------------------------

CHUNKS_DIR = r"E:\POLO\Chautha Mic\chunks"

COLLECTION_NAME = "teen_taal_chunks"

BATCH_SIZE = 50

# ---------------------------------------
# ENV
# ---------------------------------------

load_dotenv()

QDRANT_URL = os.getenv("QDRANT_URL")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")

# ---------------------------------------
# CLIENT
# ---------------------------------------

client = QdrantClient(
    url=QDRANT_URL,
    api_key=QDRANT_API_KEY
)

# ---------------------------------------
# MODEL
# ---------------------------------------

print("Loading embedding model...")

model = SentenceTransformer(
    "BAAI/bge-small-en-v1.5"
)

print("Model Loaded")

# ---------------------------------------
# FILES
# ---------------------------------------

files = [
    f for f in os.listdir(CHUNKS_DIR)
    if f.endswith(".json")
]

print(f"Found {len(files)} chunks")

# ---------------------------------------
# INGEST
# ---------------------------------------

batch = []

for idx, filename in enumerate(
    tqdm(files)
):

    path = os.path.join(
        CHUNKS_DIR,
        filename
    )

    with open(
        path,
        "r",
        encoding="utf-8"
    ) as f:

        chunk = json.load(f)

    vector = model.encode(
        chunk["text"],
        normalize_embeddings=True
    ).tolist()

    point = PointStruct(
        id=idx,
        vector=vector,
        payload=chunk
    )

    batch.append(point)

    if len(batch) >= BATCH_SIZE:

        client.upsert(
            collection_name=COLLECTION_NAME,
            points=batch
        )

        batch = []

# remaining

if batch:

    client.upsert(
        collection_name=COLLECTION_NAME,
        points=batch
    )

print()
print("Ingestion Complete")