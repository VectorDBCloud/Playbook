import os
import requests
import sys
import json

# Get API URL and key from environment variables
API_URL = os.getenv('VECTORDBCLOUD_CHROMADB_API_URL')
API_KEY = os.getenv('VECTORDBCLOUD_CHROMADB_API_KEY')

def get_tenant(tenant_name):
    if not API_URL or not API_KEY:
        print("Error: API URL or API Key not set in environment variables.")
        sys.exit(1)

    url = f"{API_URL}/api/v1/tenants/{tenant_name}"
    
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        print(f"Successfully retrieved information for tenant '{tenant_name}'.")
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error retrieving tenant information: {e}")
        sys.exit(1)

if __name__ == "__main__":
    tenant_name = "my_tenant"
    result = get_tenant(tenant_name)
    print(f"Tenant details: {json.dumps(result, indent=2)}")
