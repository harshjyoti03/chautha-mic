from fastapi import FastAPI
import json

from backend.search_episode import search_episodes

app = FastAPI()

from backend.related_episode import (
    get_related_episodes
)

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

    data = episode_index[episode_id]

    return {

        "episode_id": episode_id,

        "title": data["title"],

        "season": data["season"],

        "episode": data["episode"],

        "part": data["part"],

        "bonus": data["bonus"],

        "word_count": data["word_count"],

        "preview": data["text"][:1000],

        "text": data["text"]
    }

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