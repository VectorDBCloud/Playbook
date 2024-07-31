import requests

url = "https://your-vector-db-cloud-url.com/api/v1/collections/{collection_id}/delete"
response = requests.delete(url, json={
    "vector_db": "my_vector_db",
    "collection_id": "collection1",
    "custom_delete": lambda x: x + 1
})
assert response.status_code == 200
