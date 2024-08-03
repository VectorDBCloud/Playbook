import os
import requests
import sys
import json

# Get API URL and key from environment variables
API_URL = os.getenv('VECTORDBCLOUD_QDRANT_API_URL')
API_KEY = os.getenv('VECTORDBCLOUD_QDRANT_API_KEY')

def search_with_custom_query(collection_name, query_vector, filter_params, limit=10):
    if not API_URL or not API_KEY:
        print("Error: API URL or API Key not set in environment variables.")
        sys.exit(1)

    url = f"{API_URL}/collections/{collection_name}/points/search"
    
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "vector": query_vector,
        "filter": filter_params,
        "limit": limit
    }
    
    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        print(f"Search in collection '{collection_name}' completed successfully.")
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error performing search: {e}")
        sys.exit(1)

if __name__ == "__main__":
    collection_name = "collection1"
    query_vector = [0.1, 0.2, 0.3]  # Replace with your actual query vector
    filter_params = {
        "must": [
            {
                "key": "metadata_field",
                "match": {
                    "value": "some_value"
                }
            }
        ]
    }
    
    result = search_with_custom_query(collection_name, query_vector, filter_params)
    print(f"Search results: {json.dumps(result, indent=2)}")
