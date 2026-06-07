# backend/test_gemini.py

from backend.gemini_adapter import ask_gemini

result = ask_gemini(
    "Say hello in one sentence."
)

print(result)