import os
import re
import json

TRANSCRIPTS_DIR = r"E:\POLO\Chautha Mic\transcripts"

metadata = []

for filename in os.listdir(TRANSCRIPTS_DIR):

    if not filename.endswith(".txt"):
        continue

    item = {
        "filename": filename,
        "season": None,
        "episode": None,
        "part": None,
        "bonus": False,
        "title": None
    }

    bonus_match = re.match(
        r"s(\d+)_bonus(\d+)-(.+)\.txt",
        filename,
        re.IGNORECASE
    )

    if bonus_match:

        season, bonus_no, title = bonus_match.groups()

        item.update({
            "season": int(season),
            "episode": int(bonus_no),
            "bonus": True,
            "title": title
        })

    else:

        episode_match = re.match(
            r"s(\d+)_e(\d+)(?:_p(\d+))?-(.+)\.txt",
            filename,
            re.IGNORECASE
        )

        if episode_match:

            season, episode, part, title = episode_match.groups()

            item.update({
                "season": int(season),
                "episode": int(episode),
                "part": int(part) if part else None,
                "title": title
            })

    metadata.append(item)

output_path = r"E:\POLO\Chautha Mic\metadata\episode_metadata.json"

with open(output_path, "w", encoding="utf-8") as f:

    json.dump(
        metadata,
        f,
        ensure_ascii=False,
        indent=2
    )

print(f"Saved metadata for {len(metadata)} files")