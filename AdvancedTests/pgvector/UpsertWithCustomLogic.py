import os
import requests
import sys
import json
from sentence_transformers import SentenceTransformer

# Get API URL and key from environment variables
API_URL = os.getenv('VECTORDBCLOUD_PGVECTOR_API_URL')
API_KEY = os.getenv('VECTORDBCLOUD_PGVECTOR_API_KEY')

def upsert_with_custom_logic(collection_name, text, metadata=None):
    if not API_URL or not API_KEY:
        print("Error: API URL or API Key not set in environment variables.")
        sys.exit(1)

    url = f"{API_URL}/api/v1/collections/{collection_name}/upsert"
    
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    # Initialize the sentence transformer model
    model = SentenceTransformer('all-MiniLM-L6-v2')
    
    # Generate embedding for the text
    vector = model.encode(text).tolist()
    
    # Custom logic: Add a constant value to each element of the vector
    custom_vector = [v + 0.1 for v in vector]
    
    payload = {
        "vectors": [custom_vector],
        "metadatas": [metadata] if metadata else None,
        "documents": [text]
    }
    
    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        print(f"Upsert to collection '{collection_name}' completed successfully.")
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error performing upsert: {e}")
        sys.exit(1)

if __name__ == "__main__":
    collection_name = "my_collection"
    text = "This is a sample text for upsert"
    metadata = {"source": "example"}
    
    result = upsert_with_custom_logic(collection_name, text, metadata)
    print(f"Upsert result: {json.dumps(result, indent=2)}")
