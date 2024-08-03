import os
import requests
import sys
import json

# Get API URL and key from environment variables
API_URL = os.getenv('VECTORDBCLOUD_QDRANT_API_URL')
API_KEY = os.getenv('VECTORDBCLOUD_QDRANT_API_KEY')

def delete_collection_with_custom_logic(collection_id, custom_delete_logic):
    if not API_URL or not API_KEY:
        print("Error: API URL or API Key not set in environment variables.")
        sys.exit(1)

    url = f"{API_URL}/collections/{collection_id}"
    
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    # Convert the custom_delete_logic function to a string representation
    custom_delete_str = f"lambda x: {custom_delete_logic}"
    
    params = {
        "custom_delete": custom_delete_str
    }
    
    try:
        response = requests.delete(url, headers=headers, params=params)
        response.raise_for_status()
        print(f"Collection '{collection_id}' deleted successfully with custom logic.")
        return response.json() if response.text else {"status": "success"}
    except requests.exceptions.RequestException as e:
        print(f"Error deleting collection: {e}")
        sys.exit(1)

if __name__ == "__main__":
    collection_id = "collection1"
    custom_delete_logic = "x + 1"  # This will be converted to "lambda x: x + 1"
    
    result = delete_collection_with_custom_logic(collection_id, custom_delete_logic)
    print(f"Delete result: {json.dumps(result, indent=2)}")
