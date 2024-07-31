import requests

url = "https://your-vector-db-cloud-url.com/api/v1/collections"
response = requests.post(url, json={
    "name": "my_collection",
    "indexing": {"type": "custom", "params": {"custom_indexing_params": "..."}}
