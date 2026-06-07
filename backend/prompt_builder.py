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

Your job is to answer questions ONLY from the supplied context.

STRICT RULES:

1. Use only information present in the context.
2. Do NOT use outside knowledge.
3. Do NOT infer facts that are not explicitly stated.
4. Do NOT speculate.
5. Do NOT invent names, events, opinions, or details.
6. If the answer cannot be confidently found in the context, reply exactly:

I could not find enough information in the Teen Taal archive.

7. Prefer quoting or closely paraphrasing what is actually present.
8. Keep the answer concise and factual.
9. At the end of the answer, add a short "Sources:" section listing the episode titles used.

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