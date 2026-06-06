from sentence_transformers import SentenceTransformer

print("Loading model...")

model = SentenceTransformer(
    "BAAI/bge-m3"
)

dimension = model.get_sentence_embedding_dimension()

print()
print("Embedding Dimension:")
print(dimension)