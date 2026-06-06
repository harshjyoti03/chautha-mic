from sentence_transformers import SentenceTransformer

print("Loading multilingual-e5-base...")

embedding_model = SentenceTransformer(
    "intfloat/multilingual-e5-base"
)

print("Embedding model loaded")