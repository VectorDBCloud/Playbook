![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)
![Python](https://img.shields.io/badge/python-3.7%2B-green.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## Table of Contents

- [Advanced Tests](#advanced-tests)
- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Supported Vector Databases](#supported-vector-databases)
- [Test Scenarios by Database](#test-scenarios-by-database)
  - [pgvector](#pgvector)
  - [ChromaDB](#chromadb)
  - [Milvus](#milvus)
  - [Qdrant](#qdrant)
- [Usage](#usage)
- [Important Notes](#important-notes)
- [Advanced Functions by Database](#advanced-functions-by-database)
  - [pgvector](#pgvector-1)
  - [ChromaDB](#chromadb-1)
  - [Milvus](#milvus-1)
  - [Qdrant](#qdrant-1)
- [Interpreting Test Results](#interpreting-test-results)
- [Troubleshooting](#troubleshooting)
- [Contribution and Feedback](#contribution-and-feedback)
- [Disclaimer](#disclaimer)

# Advanced Tests

This folder contains a collection of advanced test scenarios for Vector Databases, focusing on complex functionalities and optimizations. These tests explore advanced use cases and push the capabilities of the databases.

## Introduction

Vector Database Cloud is a platform that provides managed vector database services for various vector database technologies. The advanced tests in this repository cover scenarios beyond basic operations, including custom indexing, complex queries, and custom logic for operations like upsert. These tests help in understanding the advanced features and capabilities of the Vector Databases when used with Vector Database Cloud.

## Prerequisites

- Python 3.7+
- `requests` library
- `numpy` library
- `sentence-transformers` library

Install the required libraries using:
```
pip install requests numpy sentence-transformers
```

## Supported Vector Databases

- pgvector
- ChromaDB
- Milvus
- Qdrant

## Test Scenarios by Database

### pgvector
- Create a Collection with Custom Indexing
- Search with Embeddings
- Upsert with Custom Logic

### ChromaDB
- Create a Tenant with Custom Permissions
- Search with Custom Query
- Upsert with Custom Logic

### Milvus
- Create a Collection with Custom Indexing

### Qdrant
- Create a Tenant with Custom Permissions
- Delete Collection with Custom Logic
- Get Collection with Custom Filter
- Search with Custom Query
- Upsert with Custom Logic

## Usage

To run these tests, you need to set up your environment with the Vector Database Cloud API URL and API Key for each database. For example:

```
export VECTORDBCLOUD_PGVECTOR_API_URL="https://your-pgvector-cloud-url.com"
export VECTORDBCLOUD_PGVECTOR_API_KEY="your-pgvector-api-key"
```

Then, you can run each script individually:

```
python <database_name>/<script_name>.py
```

## Important Notes

1. These scripts are examples and may need to be adapted to your specific Vector Database Cloud setup and database configuration.
2. Always ensure you're following best practices for security when handling API keys and sensitive data.
3. The exact API endpoints and payload structures may vary depending on your specific Vector Database Cloud implementation. Adjust as necessary.


## Advanced Functions by Database

### pgvector

- **`create_collection_with_custom_indexing(collection_name, indexing_params)`**: Creates a new collection with custom indexing parameters.
  - **Example**: `create_collection_with_custom_indexing("my_collection", {"index_type": "ivfflat", "lists": 100, "probe": 10})`
  - **Returns**: Details of the created collection.

- **`search_with_embeddings(query_text, collection_name, top_k=5)`**: Searches for similar vectors using text query.
  - **Example**: `search_with_embeddings("hello world", "my_collection", top_k=3)`
  - **Returns**: List of similar vectors and their metadata.

- **`upsert_with_custom_logic(collection_name, text, metadata=None)`**: Inserts or updates a vector with custom logic applied.
  - **Example**: `upsert_with_custom_logic("my_collection", "This is a sample text", {"source": "example"})`
  - **Returns**: Result of the upsert operation.

### ChromaDB

- **`create_tenant_with_custom_permissions(tenant_name, read_permissions, write_permissions)`**: Creates a new tenant with specified permissions.
  - **Example**: `create_tenant_with_custom_permissions("my_tenant", ["collection1"], ["collection2"])`
  - **Returns**: Details of the created tenant.

- **`search_with_custom_query(collection_name, query_vector, filter_params, limit=10)`**: Performs a search with custom query and filter.
  - **Example**: `search_with_custom_query("my_collection", [0.1, 0.2, 0.3], {"must": [{"key": "metadata_field", "match": {"value": "some_value"}}]})`
  - **Returns**: List of search results.

- **`upsert_with_custom_logic(collection_name, text, metadata=None)`**: Inserts or updates a vector with custom logic applied.
  - **Example**: `upsert_with_custom_logic("my_collection", "This is a sample text", {"source": "example"})`
  - **Returns**: Result of the upsert operation.

### Milvus

- **`create_collection_with_custom_indexing(collection_name, indexing_params)`**: Creates a new collection with custom indexing parameters.
  - **Example**: `create_collection_with_custom_indexing("my_collection", {"index_type": "IVF_FLAT", "metric_type": "L2", "params": {"nlist": 1024}})`
  - **Returns**: Details of the created collection.

### Qdrant

- **`create_tenant_with_custom_permissions(tenant_name, read_permissions, write_permissions)`**: Creates a new tenant with specified permissions.
  - **Example**: `create_tenant_with_custom_permissions("my_tenant", ["collection1"], ["collection2"])`
  - **Returns**: Details of the created tenant.

- **`delete_collection_with_custom_logic(collection_id, custom_delete_logic)`**: Deletes a collection using custom logic.
  - **Example**: `delete_collection_with_custom_logic("collection1", "x + 1")`
  - **Returns**: Result of the delete operation.

- **`get_collection_with_custom_filter(collection_id, filter_params)`**: Retrieves collection details using a custom filter.
  - **Example**: `get_collection_with_custom_filter("collection1", {"must": [{"key": "metadata_field", "match": {"value": "some_value"}}]})`
  - **Returns**: Collection details matching the filter.

- **`search_with_custom_query(collection_name, query_vector, filter_params, limit=10)`**: Performs a search with custom query and filter.
  - **Example**: `search_with_custom_query("my_collection", [0.1, 0.2, 0.3], {"must": [{"key": "metadata_field", "match": {"value": "some_value"}}]}, limit=5)`
  - **Returns**: List of search results.

- **`upsert_with_custom_logic(collection_name, point_id, vector, payload, custom_upsert_logic)`**: Inserts or updates a vector with custom logic applied.
  - **Example**: `upsert_with_custom_logic("my_collection", 1, [0.1, 0.2, 0.3], {"metadata": "value"}, lambda x: x + 0.1)`
  - **Returns**: Result of the upsert operation.

 
## Interpreting Test Results

After running the tests, you'll receive output detailing the performance and behavior of each operation. Key aspects to look for include:

- Successful creation of collections/tenants with custom parameters
- Accurate search results matching the given queries
- Correct application of custom logic in upsert operations
- Proper handling of custom filters and delete operations

 ## Troubleshooting

If you encounter issues:

1. Ensure all environment variables are correctly set.
2. Check your internet connection and API endpoint accessibility.
3. Verify that you have the correct permissions for the Vector Database Cloud services.
4. For specific error messages, refer to the documentation of the respective vector database or create an issue in this repository.

Common issues and solutions:
- "API key not recognized": Double-check your API key and ensure it's set correctly in the environment variables.
- "Collection not found": Verify that you're using the correct collection name and that it exists in your Vector Database Cloud instance.
- "Invalid vector dimension": Ensure that the dimension of your vectors matches the dimension specified when creating the collection.

 
## Contribution and Feedback

We encourage contributions to enhance these advanced test scenarios. For contributing new tests or suggesting improvements, please refer to our [Contribution Guidelines](../CONTRIBUTING.md). If you encounter issues or have suggestions, please use the issue tracker.


## Disclaimer

These scripts are provided as examples and may need to be adapted to your specific use case and production environment. They are not guaranteed to work in all scenarios and should be thoroughly tested before use in any critical or production systems. Always follow best practices for security and performance when working with databases and APIs. The authors and contributors of this repository are not responsible for any damages or losses that may result from the use of these scripts.
