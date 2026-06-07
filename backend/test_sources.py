from backend.ask import ask

result = ask(
    "Mirzapur"
)

print()

print("===== SOURCES =====")

print()

for source in result["sources"]:

    print(
        source["episode_id"]
    )

    print(
        source["title"]
    )

    print("-" * 80)