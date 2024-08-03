import os
import requests
import sys
import json

# Get API URL and key from environment variables
API_URL = os.getenv('VECTORDBCLOUD_CHROMADB_API_URL')
API_KEY = os.getenv('VECTORDBCLOUD_CHROMADB_API_KEY')

def upsert_with_custom_logic(collection_id, vector, custom_upsert_logic):
    if not API_URL or not API_KEY:
        print("Error: API URL or API Key not set in environment variables.")
        sys.exit(1)

    url = f"{API_URL}/api/v1/collections/{collection_id}/upsert"
    
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    # Convert the custom_upsert_logic function to a string representation
    custom_upsert_str = "lambda x: " + custom_upsert_logic
    
    payload = {
        "vector": vector,
        "custom_upsert": custom_upsert_str
    }
    
    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        print(f"Upsert to collection '{collection_id}' completed successfully.")
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error performing upsert: {e}")
        sys.exit(1)

if __name__ == "__main__":
    collection_id = "collection1"
    vector = [1, 2, 3]
    custom_upsert_logic = "x + 1"  # This will be converted to "lambda x: x + 1"
    
    result = upsert_with_custom_logic(collection_id, vector, custom_upsert_logic)
    print(f"Upsert result: {result}")
