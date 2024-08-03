import os
import requests
import sys
import json

# Get API URL and key from environment variables
API_URL = os.getenv('VECTORDBCLOUD_QDRANT_API_URL')
API_KEY = os.getenv('VECTORDBCLOUD_QDRANT_API_KEY')

def create_tenant_with_custom_permissions(tenant_name, read_permissions, write_permissions):
    if not API_URL or not API_KEY:
        print("Error: API URL or API Key not set in environment variables.")
        sys.exit(1)

    url = f"{API_URL}/api/v1/tenants"
    
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "name": tenant_name,
        "permissions": {
            "read": read_permissions,
            "write": write_permissions
        }
    }
    
    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        print(f"Tenant '{tenant_name}' created successfully with custom permissions.")
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error creating tenant: {e}")
        sys.exit(1)

if __name__ == "__main__":
    tenant_name = "my_tenant"
    read_permissions = ["collection1", "collection2"]
    write_permissions = ["collection3", "collection4"]
    
    result = create_tenant_with_custom_permissions(tenant_name, read_permissions, write_permissions)
    print(f"Tenant details: {json.dumps(result, indent=2)}")
