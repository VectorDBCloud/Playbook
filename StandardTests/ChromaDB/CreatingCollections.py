import requests

url = "https://your-vector-db-cloud-url.com/api/v1/collections"
response = requests.post(url, json={"name": "my_collection", "vector_db": "my_chromadb"})
assert response.status_code == 201
