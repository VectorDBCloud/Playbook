import os
import requests
import sys
import json

# Get API URL and key from environment variables
API_URL = os.getenv('VECTORDBCLOUD_QDRANT_API_URL')
API_KEY = os.getenv('VECTORDBCLOUD_QDRANT_API_KEY')

def delete_deployment(deployment_name):
    if not API_URL or not API_KEY:
        print("Error: API URL or API Key not set in environment variables.")
        sys.exit(1)

    url = f"{API_URL}/api/v1/deployments"
    
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "name": deployment_name
    }
    
    try:
        response = requests.delete(url, json=payload, headers=headers)
        response.raise_for_status()
        print(f"Deployment '{deployment_name}' deleted successfully.")
        return response.json() if response.text else {"status": "success"}
    except requests.exceptions.RequestException as e:
        print(f"Error deleting deployment: {e}")
        sys.exit(1)

if __name__ == "__main__":
    deployment_name = "my_qdrant"
    result = delete_deployment(deployment_name)
    print(f"Deletion result: {json.dumps(result, indent=2)}")
