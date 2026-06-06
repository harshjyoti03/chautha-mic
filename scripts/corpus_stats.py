import os
import json

JSON_DIR = r"E:\POLO\Chautha Mic\transcripts_json"

total_files = 0
total_words = 0
total_chars = 0

longest_episode = None
shortest_episode = None

max_words = 0
min_words = float("inf")

for filename in os.listdir(JSON_DIR):

    if not filename.endswith(".json"):
        continue

    path = os.path.join(JSON_DIR, filename)

    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    words = data["word_count"]
    chars = data["char_count"]

    total_files += 1
    total_words += words
    total_chars += chars

    if words > max_words:
        max_words = words
        longest_episode = filename

    if words < min_words:
        min_words = words
        shortest_episode = filename

avg_words = total_words / total_files
avg_chars = total_chars / total_files

print("\n===== CORPUS STATS =====\n")

print(f"Files: {total_files}")
print(f"Total Words: {total_words:,}")
print(f"Total Characters: {total_chars:,}")

print(f"\nAverage Words/Episode: {avg_words:,.0f}")
print(f"Average Chars/Episode: {avg_chars:,.0f}")

print("\nLongest Episode:")
print(longest_episode)
print(f"{max_words:,} words")

print("\nShortest Episode:")
print(shortest_episode)
print(f"{min_words:,} words")