import os
import json
from tqdm import tqdm
from sentence_transformers import SentenceTransformer

CHUNKS_DIR = r"E:\POLO\Chautha Mic\chunks"
OUTPUT_DIR = r"E:\POLO\Chautha Mic\embeddings"

os.makedirs(OUTPUT_DIR, exist_ok=True)

print("Loading model...")

model = SentenceTransformer(
    "BAAI/bge-m3"
)

files = [
    f for f in os.listdir(CHUNKS_DIR)
    if f.endswith(".json")
]

for filename in tqdm(files):

    path = os.path.join(
        CHUNKS_DIR,
        filename
    )

    with open(path, "r", encoding="utf-8") as f:
        chunk = json.load(f)

    embedding = model.encode(
        chunk["text"],
        normalize_embeddings=True
    )

    result = {
        "chunk_id": chunk["chunk_id"],
        "embedding": embedding.tolist()
    }

    output_file = os.path.join(
        OUTPUT_DIR,
        filename
    )

    with open(
        output_file,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(result, f)

print("Done")