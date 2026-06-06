import os
import re
import json
from tqdm import tqdm

INPUT_DIR = r"E:\POLO\Chautha Mic\transcripts_clean"
OUTPUT_DIR = r"E:\POLO\Chautha Mic\transcripts_json"

os.makedirs(OUTPUT_DIR, exist_ok=True)

for filename in tqdm(os.listdir(INPUT_DIR)):

    if not filename.endswith(".txt"):
        continue

    file_path = os.path.join(INPUT_DIR, filename)

    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read().strip()

    metadata = {
        "episode_id": None,
        "filename": filename,
        "season": None,
        "episode": None,
        "part": None,
        "bonus": False,
        "title": None,
        "word_count": len(text.split()),
        "char_count": len(text),
        "text": text
    }

    # --------------------------------------------------
    # BONUS EPISODES
    # --------------------------------------------------

    bonus_match = re.match(
        r"s(\d+)_bonus(\d+)-(.+)\.txt",
        filename,
        re.IGNORECASE
    )

    if bonus_match:

        season, bonus_no, title = bonus_match.groups()

        season = int(season)
        bonus_no = int(bonus_no)

        metadata.update({
            "episode_id": f"s{season:02d}_bonus{bonus_no:02d}",
            "season": season,
            "episode": bonus_no,
            "bonus": True,
            "title": title
        })

    else:

        # --------------------------------------------------
        # NORMAL EPISODES (+ PARTS)
        # --------------------------------------------------

        ep_match = re.match(
            r"s(\d+)_e(\d+)(?:_p(\d+))?-(.+)\.txt",
            filename,
            re.IGNORECASE
        )

        if ep_match:

            season, episode, part, title = ep_match.groups()

            season = int(season)
            episode = int(episode)

            if part:

                part = int(part)

                episode_id = (
                    f"s{season:02d}_e{episode:03d}_p{part}"
                )

            else:

                episode_id = (
                    f"s{season:02d}_e{episode:03d}"
                )

            metadata.update({
                "episode_id": episode_id,
                "season": season,
                "episode": episode,
                "part": part,
                "title": title
            })

    output_name = filename.replace(".txt", ".json")

    output_path = os.path.join(
        OUTPUT_DIR,
        output_name
    )

    with open(
        output_path,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            metadata,
            f,
            ensure_ascii=False,
            indent=2
        )

print("JSON Generation Complete")