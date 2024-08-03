import os
import requests
import sys
import json
import numpy as np
from sentence_transformers import SentenceTransformer

# Get API URL and key from environment variables
API_URL = os.getenv('VECTORDBCLOUD_PGVECTOR_API_URL')
API_KEY = os.getenv('VECTORDBCLOUD_PGVECTOR_API_KEY')

def search_with_embeddings(query_text, collection_name, top_k=5):
    if not API_URL or not API_KEY:
        print("Error: API URL or API Key not set in environment variables.")
        sys.exit(1)

    url = f"{API_URL}/api/v1/collections/{collection_name}/search"
    
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    # Initialize the sentence transformer model
    model = SentenceTransformer('all-MiniLM-L6-v2')
    
    # Generate embedding for the query text
    query_embedding = model.encode(query_text).tolist()
    
    payload = {
        "vector": query_embedding,
        "top_k": top_k
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
    query_text = "hello world"
    collection_name = "my_collection"
    
    result = search_with_embeddings(query_text, collection_name)
    print(f"Search results: {json.dumps(result, indent=2)}")
