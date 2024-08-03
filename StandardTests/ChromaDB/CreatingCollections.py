import os
import requests
import sys
import json

# Get API URL and key from environment variables
API_URL = os.getenv('VECTORDBCLOUD_CHROMADB_API_URL')
API_KEY = os.getenv('VECTORDBCLOUD_CHROMADB_API_KEY')

def create_collection(collection_name, vector_db):
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
        "vector_db": vector_db
    }
    
    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        print(f"Collection '{collection_name}' created successfully in vector database '{vector_db}'.")
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error creating collection: {e}")
        sys.exit(1)

if __name__ == "__main__":
    collection_name = "my_collection"
    vector_db = "my_chromadb"
    result = create_collection(collection_name, vector_db)
    print(f"Collection details: {json.dumps(result, indent=2)}")
