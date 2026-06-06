import json
from pathlib import Path
from tqdm import tqdm

TRANSCRIPTS = Path("transcripts_json")
OUTPUT = Path("metadata/episode_index.json")

episodes = {}

for file in tqdm(list(TRANSCRIPTS.glob("*.json"))):

    with open(
        file,
        "r",
        encoding="utf-8"
    ) as f:

        data = json.load(f)

    episode_id = f"s{data['season']:02d}"

    if data["bonus"]:

        episode_id += (
            f"_bonus{data['episode']:02d}"
        )

    else:

        episode_id += (
            f"_e{data['episode']:03d}"
        )

        if data["part"]:

            episode_id += (
                f"_p{data['part']}"
            )

    episodes[episode_id] = {

        "title":
            data["title"],

        "season":
            data["season"],

        "episode":
            data["episode"],

        "part":
            data["part"],

        "bonus":
            data["bonus"],

        "word_count":
            len(
                data["text"].split()
            ),

        "path":
            str(
                file.resolve()
            )
    }

with open(
    OUTPUT,
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        episodes,
        f,
        ensure_ascii=False
    )

print(
    f"Saved {len(episodes)} episodes"
)