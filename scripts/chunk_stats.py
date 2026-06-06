import os
import json

CHUNKS_DIR = r"E:\POLO\Chautha Mic\chunks"

total_chunks = 0
total_words = 0

largest_chunk = None
largest_words = 0

smallest_chunk = None
smallest_words = float("inf")

for filename in os.listdir(CHUNKS_DIR):

    if not filename.endswith(".json"):
        continue

    path = os.path.join(CHUNKS_DIR, filename)

    with open(path, "r", encoding="utf-8") as f:
        chunk = json.load(f)

    words = chunk["word_count"]

    total_chunks += 1
    total_words += words

    if words > largest_words:
        largest_words = words
        largest_chunk = filename

    if words < smallest_words:
        smallest_words = words
        smallest_chunk = filename

print("\n===== CHUNK STATS =====\n")

print(f"Chunks: {total_chunks}")
print(f"Average Size: {total_words/total_chunks:.2f} words")

print("\nLargest Chunk:")
print(largest_chunk)
print(largest_words)

print("\nSmallest Chunk:")
print(smallest_chunk)
print(smallest_words)