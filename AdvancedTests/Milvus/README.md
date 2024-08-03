![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)
![Python](https://img.shields.io/badge/python-3.7%2B-green.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

# Advanced Tests for Milvus

This folder contains advanced test scenarios and usage examples for Milvus, focusing on complex operations and optimizations. These tests explore the advanced capabilities of Milvus and provide guidance on maximizing its performance and functionality.

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

The advanced tests for Milvus include scenarios such as performance benchmarking, handling complex queries, optimizing indexing strategies, and testing scalability. These scenarios are designed to evaluate the database's advanced features and to push its limits under various conditions within the Vector Database Cloud environment.

## Prerequisites

- Python 3.7+
- `requests` library
- `pymilvus` library
- Access to Vector Database Cloud with API URL and API key for Milvus

Install the required libraries using:
```
pip install requests pymilvus
```

## Test Scenarios

### Create a Collection with Custom Indexing
- **Purpose**: Demonstrates how to create collections with custom indexing strategies.
- **File**: `CreateACollectionWithCustomIndexing.py`

## Usage

To run these tests, you need to set up your environment with the Vector Database Cloud API URL and API Key:

```
export VECTORDBCLOUD_MILVUS_API_URL="https://your-vector-db-cloud-url.com"
export VECTORDBCLOUD_MILVUS_API_KEY="your-api-key"
```

Then, you can run each script individually:

```
python <script_name>.py
```

## Important Notes

1. These scripts are examples and may need to be adapted to your specific Vector Database Cloud setup and Milvus configuration.
2. Always ensure you're following best practices for security when handling API keys and sensitive data.
3. The exact API endpoints and payload structures may vary depending on your specific Vector Database Cloud implementation. Adjust as necessary.

## Advanced Functions

- **`create_collection_with_custom_indexing(collection_name, indexing_params)`**: Creates a new collection with custom indexing parameters.
  - **Example**: `create_collection_with_custom_indexing("my_collection", {"index_type": "IVF_FLAT", "metric_type": "L2", "params": {"nlist": 1024}})`
  - **Returns**: Details of the created collection.

## Interpreting Test Results

After running the tests, you'll receive output detailing the performance and behavior of each operation. Key aspects to look for include:

- Successful creation of collections with custom indexing parameters
- Performance metrics for indexing and search operations
- Scalability indicators under different data loads

## Troubleshooting

If you encounter issues:

1. Ensure all environment variables are correctly set.
2. Check your internet connection and API endpoint accessibility.
3. Verify that you have the correct permissions for the Vector Database Cloud services.
4. For specific error messages, refer to the Milvus documentation or create an issue in this repository.

Common issues and solutions:
- "API key not recognized": Double-check your API key and ensure it's set correctly in the environment variables.
- "Collection not found": Verify that you're using the correct collection name and that it exists in your Vector Database Cloud instance.
- "Invalid index parameters": Ensure that the indexing parameters you're using are supported by Milvus and are correctly formatted.
- "Dimension mismatch": Verify that the dimension of your vectors matches the dimension specified when creating the collection.


## Contribution and Feedback

We welcome contributions to enhance these advanced test scenarios. Please refer to our Contribution Guidelines for more information. If you encounter any issues or have suggestions, please use the issue tracker.


## Disclaimer

These scripts are provided as examples and may need to be adapted to your specific use case and production environment. They are not guaranteed to work in all scenarios and should be thoroughly tested before use in any critical or production systems. Always follow best practices for security and performance when working with databases and APIs. The authors and contributors of this repository are not responsible for any damages or losses that may result from the use of these scripts.
