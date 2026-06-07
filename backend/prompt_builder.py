from backend.context_builder import (
    build_context
)


def build_prompt(
    question,
    context_limit=8
):

    context = build_context(
        question,
        limit=context_limit
    )

    prompt = f"""
You are an expert assistant for the Teen Taal podcast archive.

Answer ONLY using the provided context.

If the answer is not present in the context, say:
"I could not find enough information in the Teen Taal archive."

Keep answers factual.

====================
CONTEXT
====================

{context}

====================
QUESTION
====================

{question}

====================
ANSWER
====================
"""

    return prompt