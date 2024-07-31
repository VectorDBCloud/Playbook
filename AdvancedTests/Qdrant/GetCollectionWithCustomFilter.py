import requests

url = "https://your-vector-db-cloud-url.com/api/v1/collections/{collection_id}"
response = requests.get(url, params={
    "filter": {"field": "collection", "operator": "EQ", "value": "collection1"}
})
assert response.status_code == 200
