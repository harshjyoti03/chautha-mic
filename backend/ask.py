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

from backend.llm_adapter import (
    generate_answer
)


def ask(
    question,
    chunk_limit=8,
    context_limit=8
):

    # =====================
    # CHUNK RETRIEVAL
    # =====================

    chunks = search_chunks(
        question,
        limit=chunk_limit
    )

    # =====================
    # SOURCES
    # =====================

    sources = build_sources(
        chunks
    )

    # =====================
    # CONTEXT
    # =====================

    context = build_context(
        question,
        limit=context_limit
    )

    # =====================
    # PROMPT
    # =====================

    prompt = build_prompt(
        question,
        context_limit=context_limit
    )

    # =====================
    # ANSWER
    # =====================

    answer = generate_answer(
        prompt
    )

    # =====================
    # RESPONSE
    # =====================

    return {

        "question":
            question,

        "answer":
            answer,

        "sources":
            sources,

        "chunks":
            chunks,

        "context":
            context,

        "prompt":
            prompt
    }