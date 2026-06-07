from backend.prompt_builder import (
    build_prompt
)

prompt = build_prompt(
    "Mirzapur ke baare mein Teen Taal ne kya kaha?"
)

print(
    prompt[:5000]
)