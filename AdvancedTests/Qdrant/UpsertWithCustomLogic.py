import os
import requests
import sys
import json

# Get API URL and key from environment variables
API_URL = os.getenv('VECTORDBCLOUD_QDRANT_API_URL')
API_KEY = os.getenv('VECTORDBCLOUD_QDRANT_API_KEY')

def upsert_with_custom_logic(collection_name, point_id, vector, payload, custom_upsert_logic):
    if not API_URL or not API_KEY:
        print("Error: API URL or API Key not set in environment variables.")
        sys.exit(1)

    url = f"{API_URL}/collections/{collection_name}/points"
    
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    # In Qdrant, we can't directly use custom upsert logic in the API call.
    # Instead, we'll apply the custom logic to the vector before sending it.
    modified_vector = [custom_upsert_logic(x) for x in vector]
    
    payload = {
        "points": [
            {
                "id": point_id,
                "vector": modified_vector,
                "payload": payload
            }
        ]
    }
    
    try:
        response = requests.put(url, json=payload, headers=headers)
        response.raise_for_status()
        print(f"Upsert to collection '{collection_name}' completed successfully.")
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error performing upsert: {e}")
        sys.exit(1)

if __name__ == "__main__":
    collection_name = "collection1"
    point_id = 1  # Unique identifier for the point
    vector = [1, 2, 3]
    payload = {"metadata": "some_value"}
    custom_upsert_logic = lambda x: x + 1
    
    result = upsert_with_custom_logic(collection_name, point_id, vector, payload, custom_upsert_logic)
    print(f"Upsert result: {json.dumps(result, indent=2)}")
