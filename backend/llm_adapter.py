from backend.gemini_adapter import (
    ask_gemini
)


def generate_answer(prompt: str):

    return ask_gemini(
        prompt
    )