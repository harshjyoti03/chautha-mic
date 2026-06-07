from backend.ask import ask

result = ask(
    "Trump ke baare mein Teen Taal ne kya kaha, aur uske nick name kya diya gaya hai?"
)

print()

print("QUESTION")

print(
    result["question"]
)

print()

print("ANSWER")

print(
    result["answer"]
)

print()

print("SOURCES")

for source in result["sources"]:

    print(
        source["episode_id"]
    )

    print(
        source["title"]
    )

    print()