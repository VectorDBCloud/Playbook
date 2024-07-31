import requests
import numpy as np

# Load pre-trained embeddings
embeddings = np.load('path/to/embeddings.npy')

# Create a search query
query = {'query': 'hello world', 'embeddings': embeddings}

# Send the search query to the VectorDB
response = requests.post('https://your-vector-db-cloud-url.com/api/v1/search', json=query)

# Assert the response contains the expected results
assert response.status_code == 200
