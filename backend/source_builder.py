def build_sources(
    chunks
):

    sources = {}

    for chunk in chunks:

        episode_id = chunk["episode_id"]

        if episode_id not in sources:

            sources[episode_id] = {

                "episode_id":
                    episode_id,

                "title":
                    chunk["title"]
            }

    return list(
        sources.values()
    )