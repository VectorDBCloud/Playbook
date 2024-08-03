import os
import requests
import sys
import json

# Get API URL and key from environment variables
API_URL = os.getenv('VECTORDBCLOUD_CHROMADB_API_URL')
API_KEY = os.getenv('VECTORDBCLOUD_CHROMADB_API_KEY')

def get_database(database_name):
    if not API_URL or not API_KEY:
        print("Error: API URL or API Key not set in environment variables.")
        sys.exit(1)

    url = f"{API_URL}/api/v1/databases/{database_name}"
    
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        print(f"Successfully retrieved information for database '{database_name}'.")
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error retrieving database information: {e}")
        sys.exit(1)

if __name__ == "__main__":
    database_name = "my_database"
    result = get_database(database_name)
    print(f"Database details: {json.dumps(result, indent=2)}")
