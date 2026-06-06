from sentence_transformers import SentenceTransformer

model = SentenceTransformer(
    "intfloat/multilingual-e5-base"
)

print(
    model.get_embedding_dimension()
)