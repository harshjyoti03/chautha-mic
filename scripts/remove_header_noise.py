import os
from tqdm import tqdm

INPUT_DIR = r"E:\POLO\Chautha Mic\transcripts_clean"

for filename in tqdm(os.listdir(INPUT_DIR)):

    if not filename.endswith(".txt"):
        continue

    path = os.path.join(INPUT_DIR, filename)

    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    cleaned = []

    for line in lines:

        line = line.strip()

        if line.startswith("Kind:"):
            continue

        if line.startswith("Language:"):
            continue

        cleaned.append(line)

    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(cleaned))

print("Header cleanup complete")