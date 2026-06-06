import os
import json

from dotenv import load_dotenv
from qdrant_client import QdrantClient

from backend.models import embedding_model

load_dotenv()

INDEX_FILE = (
    r"E:\POLO\Chautha Mic\metadata\chunk_index.json"
)

with open(
    INDEX_FILE,
    "r",
    encoding="utf-8"
) as f:

    chunk_index = json.load(f)

client = QdrantClient(
    url=os.getenv("QDRANT_URL"),
    api_key=os.getenv("QDRANT_API_KEY")
)


def search_episodes(
    query,
    top_chunks=50,
    top_episodes=10
):

    query_vector = embedding_model.encode(
        "query: " + query,
        normalize_embeddings=True
    ).tolist()

    results = client.query_points(
        collection_name="teen_taal_chunks",
        query=query_vector,
        limit=top_chunks
    )

    episodes = {}

    for point in results.points:

        payload = point.payload

        episode_id = payload["episode_id"]

        if (
            episode_id not in episodes
            or
            point.score >
            episodes[episode_id]["score"]
        ):

            episodes[episode_id] = {

                "episode_id":
                    episode_id,

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
        episodes.values(),
        key=lambda x: x["score"],
        reverse=True
    )

    return ranked[:top_episodes]