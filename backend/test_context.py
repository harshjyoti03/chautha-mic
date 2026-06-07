from backend.context_builder import (
    build_context
)

context = build_context(
    "Mirzapur"
)

print(
    context[:3000]
)