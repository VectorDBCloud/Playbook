import requests

url = "https://your-vector-db-cloud-url.com/api/v1/tenants/my_tenant"
response = requests.get(url)
assert response.status_code == 200
