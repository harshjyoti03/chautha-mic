import os
import json

from dotenv import load_dotenv
from qdrant_client import QdrantClient

from backend.models import embedding_model

load_dotenv()

EPISODE_INDEX = (
    r"E:\POLO\Chautha Mic\metadata\episode_index.json"
)

with open(
    EPISODE_INDEX,
    "r",
    encoding="utf-8"
) as f:

    episodes = json.load(f)

client = QdrantClient(
    url=os.getenv("QDRANT_URL"),
    api_key=os.getenv("QDRANT_API_KEY")
)


def get_related_episodes(
    episode_id,
    top_k=10
):

    if episode_id not in episodes:

        return []

    title = episodes[episode_id]["title"]

    query_vector = embedding_model.encode(
        "query: " + title,
        normalize_embeddings=True
    ).tolist()

    results = client.query_points(
        collection_name="teen_taal_chunks",
        query=query_vector,
        limit=100
    )

    related = {}

    for point in results.points:

        payload = point.payload

        other_episode = payload["episode_id"]

        if other_episode == episode_id:
            continue

        if (
            other_episode not in related
            or
            point.score >
            related[other_episode]["score"]
        ):

            related[other_episode] = {

                "episode_id":
                    other_episode,

                "title":
                    payload["title"],

                "score":
                    point.score,

                "season":
                    payload["season"],

                "episode":
                    payload["episode"]
            }

    ranked = sorted(
        related.values(),
        key=lambda x: x["score"],
        reverse=True
    )

    return ranked[:top_k]