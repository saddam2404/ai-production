text = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

chunk_size = 5
overlap = 2

step = chunk_size - overlap

for i in range(0, len(text), step):
    chunk = text[i:i + chunk_size]
    print(chunk)