from search_chunks import search_chunks

results = search_chunks(
    "Mirzapur"
)

for r in results:

    print()

    print(r["episode_id"])

    print(r["title"])

    print(r["score"])