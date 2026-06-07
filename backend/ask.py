from backend.search_chunks import (
    search_chunks
)

from backend.context_builder import (
    build_context
)

from backend.prompt_builder import (
    build_prompt
)

from backend.source_builder import (
    build_sources
)


def ask(
    question,
    chunk_limit=8,
    context_limit=8
):

    # =====================
    # RETRIEVE CHUNKS
    # =====================

    chunks = search_chunks(
        question,
        limit=chunk_limit
    )

    # =====================
    # BUILD SOURCES
    # =====================

    sources = build_sources(
        chunks
    )

    # =====================
    # BUILD CONTEXT
    # =====================

    context = build_context(
        question,
        limit=context_limit
    )

    # =====================
    # BUILD PROMPT
    # =====================

    prompt = build_prompt(
        question,
        context_limit=context_limit
    )

    # =====================
    # RETURN PIPELINE DATA
    # =====================

    return {

        "question":
            question,

        "chunks":
            chunks,

        "sources":
            sources,

        "context":
            context,

        "prompt":
            prompt
    }