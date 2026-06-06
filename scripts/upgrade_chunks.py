import os
import json
from tqdm import tqdm

CHUNKS_DIR = r"E:\POLO\Chautha Mic\chunks"

for filename in tqdm(os.listdir(CHUNKS_DIR)):

    if not filename.endswith(".json"):
        continue

    path = os.path.join(CHUNKS_DIR, filename)

    with open(path, "r", encoding="utf-8") as f:
        chunk = json.load(f)

    searchable_text = f"""
Title: {chunk['title']}

Episode ID: {chunk['episode_id']}

Content:

{chunk['text']}
"""

    chunk["search_text"] = searchable_text

    with open(path, "w", encoding="utf-8") as f:
        json.dump(
            chunk,
            f,
            ensure_ascii=False,
            indent=2
        )

print("Chunks upgraded")