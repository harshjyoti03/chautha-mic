import os
import json
from tqdm import tqdm

CHUNKS_DIR = r"E:\POLO\Chautha Mic\chunks"

OUTPUT_FILE = (
    r"E:\POLO\Chautha Mic\metadata\chunk_index.json"
)

index = {}

files = [
    f for f in os.listdir(CHUNKS_DIR)
    if f.endswith(".json")
]

for filename in tqdm(files):

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

    index[
        chunk["chunk_id"]
    ] = {

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
            chunk["chunk_index"],

        "path":
            path
    }

with open(
    OUTPUT_FILE,
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        index,
        f,
        ensure_ascii=False,
        indent=2
    )

print(
    f"Saved {len(index)} entries"
)