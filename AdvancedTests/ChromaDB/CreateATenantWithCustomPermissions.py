import requests

url = "https://your-vector-db-cloud-url.com/api/v1/tenants"
response = requests.post(url, json={
    "name": "my_tenant",
    "permissions": {
        "read": ["collection1", "collection2"],
        "write": ["collection3", "collection4"]
    }
})
assert response.status_code == 201
