def ask_gemini(prompt: str):

    try:

        response = model.generate_content(
            prompt
        )

        return {
            "provider": "google",
            "model": "gemini-2.5-flash",
            "answer": response.text
        }

    except Exception as e:

        return {
            "provider": "google",
            "model": "gemini-2.5-flash",
            "error": str(e),
            "answer":
                "LLM temporarily unavailable."
        }