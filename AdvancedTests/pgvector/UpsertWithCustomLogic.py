import requests

# Create a custom upsert function
def custom_upsert(vector_db, collection_id, vector):
    # Custom logic to upsert the vector
    pass

# Upsert a vector with custom logic
response = requests.post('https://your-vector-db-cloud-url.com/api/v1/collections/{collection_id}/upsert', json={
    'vector_db': vector_db,
    'collection_id': collection_id,
    'vector': vector,
    'custom_upsert': custom_upsert
})

# Assert the upsert was successful
assert response.status_code == 200
