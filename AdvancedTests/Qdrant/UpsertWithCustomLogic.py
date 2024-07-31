import requests

url = "https://your-vector-db-cloud-url.com/api/v1/collections/{collection_id}/upsert"
response = requests.post(url, json={
    "vector_db": "my_vector_db",
    "collection_id": "collection1",
    "vector": [1, 2, 3],
    "custom_upsert": lambda x: x + 1
})
assert response.status_code == 200
