import requests

url = "https://your-vector-db-cloud-url.com/api/v1/deployments"
response = requests.post(url, json={"name": "my_chromadb", "vector_db": "chromadb"})
assert response.status_code == 201