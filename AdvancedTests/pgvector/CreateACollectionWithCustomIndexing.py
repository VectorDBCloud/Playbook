import os
import requests
import sys
import json

# Get API URL and key from environment variables
API_URL = os.getenv('VECTORDBCLOUD_PGVECTOR_API_URL')
API_KEY = os.getenv('VECTORDBCLOUD_PGVECTOR_API_KEY')

def create_collection_with_custom_indexing(collection_name, indexing_params):
    if not API_URL or not API_KEY:
        print("Error: API URL or API Key not set in environment variables.")
        sys.exit(1)

    url = f"{API_URL}/api/v1/collections"
    
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "name": collection_name,
        "indexing": {
            "type": "custom",
            "params": indexing_params
        }
    }
    
    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        print(f"Collection '{collection_name}' created successfully with custom indexing.")
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error creating collection: {e}")
        sys.exit(1)

if __name__ == "__main__":
    collection_name = "my_collection"
    custom_indexing_params = {
        "index_type": "ivfflat",
        "lists": 100,
        "probe": 10
    }
    
    result = create_collection_with_custom_indexing(collection_name, custom_indexing_params)
    print(f"Collection details: {json.dumps(result, indent=2)}")
