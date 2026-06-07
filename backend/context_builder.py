from backend.evidence import (
    get_evidence
)


def build_context(
    query,
    limit=8
):

    chunks = get_evidence(
        query,
        limit=limit
    )

    context_parts = []

    for chunk in chunks:

        context_parts.append(

            f"""
Episode:
{chunk['title']}

Transcript:
{chunk['text']}
"""
        )

    return "\n\n".join(
        context_parts
    )