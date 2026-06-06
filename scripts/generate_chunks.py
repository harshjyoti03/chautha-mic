import os
import json
from tqdm import tqdm

INPUT_DIR = r"E:\POLO\Chautha Mic\transcripts_json"
OUTPUT_DIR = r"E:\POLO\Chautha Mic\chunks"

os.makedirs(OUTPUT_DIR, exist_ok=True)

CHUNK_SIZE = 1000
OVERLAP = 200

total_chunks = 0

for filename in tqdm(os.listdir(INPUT_DIR)):

    if not filename.endswith(".json"):
        continue

    path = os.path.join(INPUT_DIR, filename)

    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    words = data["text"].split()

    start = 0
    chunk_index = 1

    while start < len(words):

        end = start + CHUNK_SIZE

        chunk_words = words[start:end]

        chunk_text = " ".join(chunk_words)

        chunk = {

            "chunk_id":
                f"{data['episode_id']}_c{chunk_index:04d}",

            "episode_id":
                data["episode_id"],

            "season":
                data["season"],

            "episode":
                data["episode"],

            "part":
                data["part"],

            "bonus":
                data["bonus"],

            "title":
                data["title"],

            "chunk_index":
                chunk_index,

            "word_count":
                len(chunk_words),

            "text":
                chunk_text
        }

        chunk_filename = (
            f"{chunk['chunk_id']}.json"
        )

        with open(
            os.path.join(
                OUTPUT_DIR,
                chunk_filename
            ),
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                chunk,
                f,
                ensure_ascii=False,
                indent=2
            )

        total_chunks += 1

        chunk_index += 1

        start += (
            CHUNK_SIZE - OVERLAP
        )

print()
print(f"Generated {total_chunks} chunks")