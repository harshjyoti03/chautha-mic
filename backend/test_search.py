from backend.search_episode import search_episodes

while True:

    q = input("\nSearch > ")

    if q.lower() == "exit":
        break

    results = search_episodes(q)

    print()

    for idx, result in enumerate(
        results,
        start=1
    ):

        print(
            f"{idx}. "
            f"{result['episode_id']} "
            f"({result['score']:.4f})"
        )

        print(
            result["title"]
        )

        print()