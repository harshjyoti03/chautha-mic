import os
import re
from tqdm import tqdm

INPUT_DIR = r"E:\POLO\Chautha Mic\transcripts"
OUTPUT_DIR = r"E:\POLO\Chautha Mic\transcripts_clean"

os.makedirs(OUTPUT_DIR, exist_ok=True)

timestamp_pattern = r"<\d{2}:\d{2}:\d{2}\.\d+>"
html_pattern = r"</?c>"

for filename in tqdm(os.listdir(INPUT_DIR)):

    if not filename.endswith(".txt"):
        continue

    path = os.path.join(INPUT_DIR, filename)

    with open(path, "r", encoding="utf-8") as f:
        text = f.read()

    text = re.sub(timestamp_pattern, "", text)
    text = re.sub(html_pattern, "", text)

    cleaned_lines = []
    previous_line = ""

    for line in text.splitlines():

        line = re.sub(r"\s+", " ", line).strip()

        if len(line) < 5:
            continue

        if line == previous_line:
            continue

        cleaned_lines.append(line)
        previous_line = line

    cleaned_text = "\n".join(cleaned_lines)

    output_file = os.path.join(
        OUTPUT_DIR,
        filename
    )

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(cleaned_text)

print("Cleaning Complete")