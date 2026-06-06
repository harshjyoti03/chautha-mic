import os
import json

from tqdm import tqdm
from dotenv import load_dotenv

from sentence_transformers import SentenceTransformer

from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct

load_dotenv()

CHUNKS_DIR = r"E:\POLO\Chautha Mic\chunks"

COLLECTION_NAME = "teen_taal_chunks"

BATCH_SIZE = 25

client = QdrantClient(
    url=os.getenv("QDRANT_URL"),
    api_key=os.getenv("QDRANT_API_KEY")
)

print("Loading multilingual-e5-base...")

model = SentenceTransformer(
    "intfloat/multilingual-e5-base"
)

print("Model Loaded")

files = sorted([
    f for f in os.listdir(CHUNKS_DIR)
    if f.endswith(".json")
])

print(f"Found {len(files)} chunks")

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

    text = (
        "passage: "
        + chunk["search_text"]
    )

    vector = model.encode(
        text,
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

if batch:

    client.upsert(
        collection_name=COLLECTION_NAME,
        points=batch
    )

print("Ingestion Complete")