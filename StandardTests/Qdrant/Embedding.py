import requests

url = "https://your-vector-db-cloud-url.com/api/v1/embeddings"
response = requests.post(url, json={"vector_db": "my_qdrant", "embedding": "my_embedding"})
assert response.status_code == 200
