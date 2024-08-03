import os
import requests
import sys
import json

# Get API URL and key from environment variables
API_URL = os.getenv('VECTORDBCLOUD_QDRANT_API_URL')
API_KEY = os.getenv('VECTORDBCLOUD_QDRANT_API_KEY')

def get_collection_with_custom_filter(collection_id, filter_params):
    if not API_URL or not API_KEY:
        print("Error: API URL or API Key not set in environment variables.")
        sys.exit(1)

    url = f"{API_URL}/collections/{collection_id}"
    
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    params = {
        "filter": json.dumps(filter_params)
    }
    
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        print(f"Collection '{collection_id}' retrieved successfully with custom filter.")
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error retrieving collection: {e}")
        sys.exit(1)

if __name__ == "__main__":
    collection_id = "collection1"
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
    
    result = get_collection_with_custom_filter(collection_id, filter_params)
    print(f"Collection details: {json.dumps(result, indent=2)}")
