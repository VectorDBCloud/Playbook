import requests

url = "https://your-vector-db-cloud-url.com/api/v1/tenants"
response = requests.post(url, json={"name": "my_tenant"})
assert response.status_code == 201
