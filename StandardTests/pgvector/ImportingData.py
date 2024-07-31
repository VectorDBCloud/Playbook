import requests
import pandas as pd

url = "https://your-vector-db-cloud-url.com/api/v1/import"
data = pd.DataFrame({"id": [1, 2, 3], "vector": [[1, 2, 3], [4, 5, 6], [7, 8, 9]]})
response = requests.post(url, json={"vector_db": "my_pgvector", "data": data.to_dict()})
assert response.status_code == 200
