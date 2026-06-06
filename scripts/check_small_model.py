from sentence_transformers import SentenceTransformer

print("Loading model...")

model = SentenceTransformer(
    "BAAI/bge-small-en-v1.5"
)

print("Embedding Dimension:")
print(model.get_sentence_embedding_dimension())