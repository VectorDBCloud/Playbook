![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)
![Python](https://img.shields.io/badge/python-3.7%2B-green.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

# Advanced Tests for ChromaDB

This folder contains advanced test scenarios and usage examples for ChromaDB, focusing on complex operations and optimizations. These tests explore the advanced capabilities of ChromaDB and provide guidance on maximizing its potential.

## Introduction

The advanced tests for ChromaDB include scenarios for creating tenants with custom permissions, performing searches with custom queries, and implementing upsert operations with custom logic. These tests are designed to demonstrate the database's advanced features and explore its usage within the Vector Database Cloud environment.

## Test Scenarios

### Create a Tenant with Custom Permissions
- **Purpose**: Demonstrates how to create tenants with custom permissions.
- **File**: `CreateATenantWithCustomPermissions.py`

### Search with Custom Query
- **Purpose**: Illustrates how to perform searches using custom query logic.
- **File**: `SearchWithCustomQuery.py`

### Upsert with Custom Logic
- **Purpose**: Shows how to implement upsert operations with custom logic.
- **File**: `UpsertWithCustomLogic.py`

## Usage

To run these tests, you need to set up your environment with the Vector Database Cloud API URL and API Key:

```
export VECTORDBCLOUD_CHROMADB_API_URL="https://your-vector-db-cloud-url.com"
export VECTORDBCLOUD_CHROMADB_API_KEY="your-api-key"
```

Then, you can run each script individually:

```
python <script_name>.py
```

## Important Notes

1. These scripts are examples and may need to be adapted to your specific Vector Database Cloud setup and ChromaDB configuration.
2. Always ensure you're following best practices for security when handling API keys and sensitive data.
3. The exact API endpoints and payload structures may vary depending on your specific Vector Database Cloud implementation. Adjust as necessary.

## Advanced Functions

### Searching
- **`chromadb.advanced_search(query, vector_db)`**: Conducts advanced searches using complex criteria.
  - **Example**: `chromadb.advanced_search("deep learning models", vector_db)`
  - **Returns**: A list of search results matching the query.

### Insertion
- **`chromadb.insert_advanced(vector, vector_db)`**: Inserts a vector with additional metadata for advanced usage.
  - **Example**: `chromadb.insert_advanced([0.1, 0.5, 0.3], vector_db)`
  - **Returns**: The ID of the inserted vector.

### Update
- **`chromadb.update_vector(vector_id, new_data, vector_db)`**: Updates an existing vector's data.
  - **Example**: `chromadb.update_vector(123, [0.2, 0.6, 0.4], vector_db)`
  - **Returns**: The ID of the updated vector.

### Deletion
- **`chromadb.delete_vector(vector_id, vector_db)`**: Deletes a vector from the database.
  - **Example**: `chromadb.delete_vector(123, vector_db)`
  - **Returns**: Confirmation of deletion.


## Contribution and Feedback

We welcome contributions to enhance these advanced test scenarios. Please refer to our Contribution Guidelines for more information. If you have any issues or suggestions, feel free to use the issue tracker.


## Disclaimer

These scripts are provided as examples and may need to be adapted to your specific use case and production environment. They are not guaranteed to work in all scenarios and should be thoroughly tested before use in any critical or production systems. Always follow best practices for security and performance when working with databases and APIs. The authors and contributors of this repository are not responsible for any damages or losses that may result from the use of these scripts.
