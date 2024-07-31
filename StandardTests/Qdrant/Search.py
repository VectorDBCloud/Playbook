import requests

url = "https://your-vector-db-cloud-url.com/api/v1/search"
response = requests.post(url, json={"query": "hello world", "vector_db": "my_qdrant"})
assert response.status_code == 200
