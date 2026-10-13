from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

text = "This is a sample text to generate embeddings."

embeddings = model.encode(text) 

print("Embeddings:", embeddings)

print("Embeddings lengths:", len(embeddings))
