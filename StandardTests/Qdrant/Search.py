import os
import requests
import sys
import json
from sentence_transformers import SentenceTransformer

# Get API URL and key from environment variables
API_URL = os.getenv('VECTORDBCLOUD_QDRANT_API_URL')
API_KEY = os.getenv('VECTORDBCLOUD_QDRANT_API_KEY')

def search(query, vector_db, top_k=5):
    if not API_URL or not API_KEY:
        print("Error: API URL or API Key not set in environment variables.")
        sys.exit(1)

    url = f"{API_URL}/api/v1/search"
    
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    # Generate embedding for the query
    model = SentenceTransformer('all-MiniLM-L6-v2')
    query_embedding = model.encode(query).tolist()
    
    payload = {
        "query": query,
        "vector_db": vector_db,
        "embedding": query_embedding,
        "top_k": top_k
    }
    
    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        print(f"Search completed successfully in vector database '{vector_db}'.")
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error performing search: {e}")
        sys.exit(1)

if __name__ == "__main__":
    query = "hello world"
    vector_db = "my_qdrant"
    result = search(query, vector_db)
    print(f"Search results: {json.dumps(result, indent=2)}")
