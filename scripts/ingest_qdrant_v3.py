import os
import json
import time

from tqdm import tqdm
from dotenv import load_dotenv

from sentence_transformers import SentenceTransformer

from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct

# ==================================================
# CONFIG
# ==================================================

CHUNKS_DIR = r"E:\POLO\Chautha Mic\chunks"

PROGRESS_FILE = (
    r"E:\POLO\Chautha Mic\metadata\upload_progress.json"
)

COLLECTION_NAME = "teen_taal_chunks"

BATCH_SIZE = 10

# ==================================================
# ENV
# ==================================================

load_dotenv()

client = QdrantClient(
    url=os.getenv("QDRANT_URL"),
    api_key=os.getenv("QDRANT_API_KEY")
)

# ==================================================
# MODEL
# ==================================================

print("Loading multilingual-e5-base...")

model = SentenceTransformer(
    "intfloat/multilingual-e5-base"
)

print("Model Loaded")

# ==================================================
# FILES
# ==================================================

files = sorted([
    f for f in os.listdir(CHUNKS_DIR)
    if f.endswith(".json")
])

print(f"Found {len(files)} chunks")

# ==================================================
# LOAD PROGRESS
# ==================================================

if os.path.exists(PROGRESS_FILE):

    with open(
        PROGRESS_FILE,
        "r",
        encoding="utf-8"
    ) as f:

        progress = json.load(f)

    start_idx = (
        progress["last_uploaded"] + 1
    )

else:

    start_idx = 0

print(
    f"Resuming from {start_idx}"
)

# ==================================================
# INGEST
# ==================================================

batch = []

for idx in tqdm(
    range(start_idx, len(files))
):

    filename = files[idx]

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

    embed_text = (
        "passage: "
        + chunk["search_text"]
    )

    vector = model.encode(
        embed_text,
        normalize_embeddings=True
    ).tolist()

    payload = {

        "chunk_id":
            chunk["chunk_id"],

        "episode_id":
            chunk["episode_id"],

        "title":
            chunk["title"],

        "season":
            chunk["season"],

        "episode":
            chunk["episode"],

        "part":
            chunk["part"],

        "chunk_index":
            chunk["chunk_index"]
    }

    point = PointStruct(
        id=idx,
        vector=vector,
        payload=payload
    )

    batch.append(point)

    if len(batch) >= BATCH_SIZE:

        success = False

        while not success:

            try:

                client.upsert(
                    collection_name=
                        COLLECTION_NAME,

                    points=batch
                )

                success = True

            except Exception as e:

                print(
                    "\nRetrying:",
                    str(e)
                )

                time.sleep(5)

        with open(
            PROGRESS_FILE,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                {
                    "last_uploaded":
                        idx
                },
                f,
                indent=2
            )

        batch = []

# remaining

if batch:

    client.upsert(
        collection_name=
            COLLECTION_NAME,

        points=batch
    )

    with open(
        PROGRESS_FILE,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            {
                "last_uploaded":
                    len(files)-1
            },
            f,
            indent=2
        )

print()
print("INGESTION COMPLETE")