![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)
![Python](https://img.shields.io/badge/python-3.7%2B-green.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

# Advanced Tests for ChromaDB

This folder contains advanced test scenarios and usage examples for ChromaDB, focusing on complex operations and optimizations. These tests explore the advanced capabilities of ChromaDB and provide guidance on maximizing its potential.

## Table of Contents

- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Test Scenarios](#test-scenarios)
- [Usage](#usage)
- [Important Notes](#important-notes)
- [Advanced Functions](#advanced-functions)
- [Interpreting Test Results](#interpreting-test-results)
- [Troubleshooting](#troubleshooting)
- [Contribution and Feedback](#contribution-and-feedback)
- [Disclaimer](#disclaimer)

## Introduction

The advanced tests for ChromaDB include scenarios for creating tenants with custom permissions, performing searches with custom queries, and implementing upsert operations with custom logic. These tests are designed to demonstrate the database's advanced features and explore its usage within the Vector Database Cloud environment.

## Prerequisites

- Python 3.7+
- `requests` library
- `chromadb` library
- Access to Vector Database Cloud with API URL and API key for ChromaDB

Install the required libraries using:
```
pip install requests chromadb
```

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

- **`create_tenant_with_custom_permissions(tenant_name, read_permissions, write_permissions)`**: Creates a new tenant with specified permissions.
  - **Example**: `create_tenant_with_custom_permissions("my_tenant", ["collection1"], ["collection2"])`
  - **Returns**: Details of the created tenant.

- **`search_with_custom_query(collection_name, query_vector, filter_params, limit=10)`**: Performs a search with custom query and filter.
  - **Example**: `search_with_custom_query("my_collection", [0.1, 0.2, 0.3], {"must": [{"key": "metadata_field", "match": {"value": "some_value"}}]})`
  - **Returns**: List of search results.

- **`upsert_with_custom_logic(collection_name, text, metadata=None)`**: Inserts or updates a vector with custom logic applied.
  - **Example**: `upsert_with_custom_logic("my_collection", "This is a sample text", {"source": "example"})`
  - **Returns**: Result of the upsert operation.

## Interpreting Test Results

After running the tests, you'll receive output detailing the performance and behavior of each operation. Key aspects to look for include:

- Successful creation of tenants with custom permissions
- Accurate search results matching the given queries
- Correct application of custom logic in upsert operations

## Troubleshooting

If you encounter issues:

1. Ensure all environment variables are correctly set.
2. Check your internet connection and API endpoint accessibility.
3. Verify that you have the correct permissions for the Vector Database Cloud services.
4. For specific error messages, refer to the ChromaDB documentation or create an issue in this repository.

Common issues and solutions:
- "API key not recognized": Double-check your API key and ensure it's set correctly in the environment variables.
- "Collection not found": Verify that you're using the correct collection name and that it exists in your Vector Database Cloud instance.
- "Invalid vector dimension": Ensure that the dimension of your vectors matches the dimension specified when creating the collection.

## Contribution and Feedback

We welcome contributions to enhance these advanced test scenarios. Please refer to our Contribution Guidelines for more information. If you have any issues or suggestions, feel free to use the issue tracker.


## Disclaimer

These scripts are provided as examples and may need to be adapted to your specific use case and production environment. They are not guaranteed to work in all scenarios and should be thoroughly tested before use in any critical or production systems. Always follow best practices for security and performance when working with databases and APIs. The authors and contributors of this repository are not responsible for any damages or losses that may result from the use of these scripts.
