import requests

url = "https://your-vector-db-cloud-url.com/api/v1/deployments"
response = requests.delete(url, json={"name": "my_pgvector"})
assert response.status_code == 200