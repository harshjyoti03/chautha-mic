import json

from backend.search_chunks import (
    search_chunks
)


def get_evidence(
    query,
    limit=10
):

    results = search_chunks(
        query,
        limit=limit
    )

    evidence = []

    for result in results:

        chunk_id = result["chunk_id"]

        chunk_path = (
            rf"E:\POLO\Chautha Mic\chunks\{chunk_id}.json"
        )

        try:

            with open(
                chunk_path,
                "r",
                encoding="utf-8"
            ) as f:

                chunk = json.load(f)

            evidence.append({

                "chunk_id":
                    chunk_id,

                "episode_id":
                    chunk["episode_id"],

                "title":
                    chunk["title"],

                "score":
                    result["score"],

                "text":
                    chunk["text"]
            })

        except Exception:

            continue

    return evidence