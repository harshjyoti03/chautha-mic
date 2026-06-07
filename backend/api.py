from fastapi import FastAPI
import json

from backend.search_episode import search_episodes
from backend.related_episode import get_related_episodes

from backend.evidence import (
    get_evidence
)

app = FastAPI()

# =========================
# LOAD EPISODE INDEX
# =========================

with open(
    r"E:\POLO\Chautha Mic\metadata\episode_index.json",
    "r",
    encoding="utf-8"
) as f:

    episode_index = json.load(f)

# =========================
# ROOT
# =========================

@app.get("/")
def root():

    return {
        "status": "running"
    }

# =========================
# SEARCH
# =========================

@app.get("/search")
def search(query: str):

    results = search_episodes(query)

    return {
        "query": query,
        "results": results
    }

# =========================
# ALL EPISODES
# =========================

@app.get("/episodes")
def episodes():

    results = []

    for episode_id, data in episode_index.items():

        results.append({

            "episode_id": episode_id,

            "title": data["title"],

            "season": data["season"],

            "episode": data["episode"],

            "part": data["part"],

            "bonus": data["bonus"],

            "word_count": data["word_count"]
        })

    results = sorted(
        results,
        key=lambda x: (
            x["season"],
            x["episode"]
        )
    )

    return results

# =========================
# EPISODE DETAILS
# =========================

@app.get("/episode/{episode_id}")
def get_episode(
    episode_id: str
):

    if episode_id not in episode_index:

        return {
            "error": "Episode not found"
        }

    metadata = episode_index[episode_id]

    transcript_path = metadata["path"]

    with open(
        transcript_path,
        "r",
        encoding="utf-8"
    ) as f:

        transcript = json.load(f)

    text = transcript["text"]

    return {

        "episode_id":
            episode_id,

        "title":
            metadata["title"],

        "season":
            metadata["season"],

        "episode":
            metadata["episode"],

        "part":
            metadata["part"],

        "bonus":
            metadata["bonus"],

        "word_count":
            metadata["word_count"],

        "preview":
            text[:1000],

        "text":
            text
    }

# =========================
# RELATED EPISODES
# =========================

@app.get("/related/{episode_id}")
def related(
    episode_id: str
):

    results = get_related_episodes(
        episode_id
    )

    return {

        "episode_id":
            episode_id,

        "related":
            results
    }

@app.get("/evidence")
def evidence(
    query: str
):

    chunks = get_evidence(
        query
    )

    return {

        "query":
            query,

        "chunks":
            chunks
    }