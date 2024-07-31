import requests

url = "https://your-vector-db-cloud-url.com/api/v1/deployments"
response = requests.post(url, json={"name": "my_qdrant", "vector_db": "qdrant"})
assert response.status_code == 201
