import os
import requests
import sys

# Get API URL and key from environment variables
API_URL = os.getenv('VECTORDBCLOUD_CHROMADB_API_URL')
API_KEY = os.getenv('VECTORDBCLOUD_CHROMADB_API_KEY')

def search_with_custom_query(query, filter_condition):
    if not API_URL or not API_KEY:
        print("Error: API URL or API Key not set in environment variables.")
        sys.exit(1)

    url = f"{API_URL}/api/v1/search"
    
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "query": query,
        "filter": filter_condition
    }
    
    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        print("Search completed successfully.")
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error performing search: {e}")
        sys.exit(1)

if __name__ == "__main__":
    query = "hello world"
    filter_condition = {"field": "collection", "operator": "EQ", "value": "collection1"}
    
    result = search_with_custom_query(query, filter_condition)
    print(f"Search results: {result}")
