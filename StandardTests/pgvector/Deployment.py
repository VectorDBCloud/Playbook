import os
import requests
import sys
import json

# Get API URL and key from environment variables
API_URL = os.getenv('VECTORDBCLOUD_PGVECTOR_API_URL')
API_KEY = os.getenv('VECTORDBCLOUD_PGVECTOR_API_KEY')

def create_deployment(deployment_name, vector_db):
    if not API_URL or not API_KEY:
        print("Error: API URL or API Key not set in environment variables.")
        sys.exit(1)

    url = f"{API_URL}/api/v1/deployments"
    
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "name": deployment_name,
        "vector_db": vector_db
    }
    
    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        print(f"Deployment '{deployment_name}' created successfully with vector database '{vector_db}'.")
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error creating deployment: {e}")
        sys.exit(1)

if __name__ == "__main__":
    deployment_name = "my_pgvector"
    vector_db = "pgvector"
    result = create_deployment(deployment_name, vector_db)
    print(f"Deployment details: {json.dumps(result, indent=2)}")
