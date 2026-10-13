from sentence_transformers import SentenceTransformer
from sentence_transformers.util import cos_sim

model = SentenceTransformer('all-MiniLM-L6-v2')

sentence_a = "I build machine learning models using Python."
sentence_b = "I develop AI systems with Python."
sentence_c = "I enjoy cooking Italian food."

embeddings_a = model.encode(sentence_a)
embeddings_b = model.encode(sentence_b)
embeddings_c = model.encode(sentence_c)

similarity_ab = cos_sim(embeddings_a, embeddings_b)
similarity_ac = cos_sim(embeddings_a, embeddings_c)

print("Similarity between A and B:", similarity_ab)
print("Similarity between A and C:", similarity_ac)
