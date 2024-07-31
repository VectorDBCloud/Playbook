import requests

# Create a collection with custom indexing
collection = requests.post('https://your-vector-db-cloud-url.com/api/v1/collections', json={
    'name': 'my_collection',
    'indexing': {'type': 'custom', 'params': {'custom_indexing_params': '...'}}
})

# Assert the collection was created successfully
assert collection.status_code == 201
