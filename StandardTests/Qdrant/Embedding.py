import os
import requests
import sys
import json
from sentence_transformers import SentenceTransformer

# Get API URL and key from environment variables
API_URL = os.getenv('VECTORDBCLOUD_QDRANT_API_URL')
API_KEY = os.getenv('VECTORDBCLOUD_QDRANT_API_KEY')

def create_embedding(vector_db, text):
    if not API_URL or not API_KEY:
        print("Error: API URL or API Key not set in environment variables.")
        sys.exit(1)

    url = f"{API_URL}/api/v1/embeddings"
    
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    # Generate embedding using SentenceTransformer
    model = SentenceTransformer('all-MiniLM-L6-v2')
    embedding = model.encode(text).tolist()
    
    payload = {
        "vector_db": vector_db,
        "embedding": embedding
    }
    
    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        print(f"Embedding created successfully for vector database '{vector_db}'.")
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error creating embedding: {e}")
        sys.exit(1)

if __name__ == "__main__":
    vector_db = "my_qdrant"
    text = "This is a sample text for embedding."
    result = create_embedding(vector_db, text)
    print(f"Embedding result: {json.dumps(result, indent=2)}")
