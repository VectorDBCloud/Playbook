import requests

url = "https://your-vector-db-cloud-url.com/api/v1/databases"
response = requests.post(url, json={"name": "my_database"})
assert response.status_code == 201
