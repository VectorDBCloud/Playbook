![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)
![Python](https://img.shields.io/badge/python-3.7%2B-green.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

# Standard Tests for Vector Databases

This folder contains a collection of standard tests for various Vector Databases, including installation instructions and examples of how to use each Vector Database within the Vector Database Cloud environment.

## Table of Contents

- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Test Scenarios](#test-scenarios)
- [Using the Vector Databases](#using-the-vector-databases)
- [Troubleshooting](#troubleshooting)
- [Contribution and Feedback](#contribution-and-feedback)
- [Disclaimer](#disclaimer)

## Introduction

The standard tests folder includes a variety of tests that cover different aspects of the Vector Databases, including installation, usage, and basic features. These tests are designed to help you get started with using the Vector Databases and to provide a baseline for testing and validation within the Vector Database Cloud environment.

## Prerequisites

- Python 3.7+
- Access to Vector Database Cloud with API URL and API key for each database
- Respective Python client libraries for each vector database

Install the required libraries using:
```
pip install requests pandas sentence-transformers pgvector chromadb pymilvus qdrant-client
```

## Test Scenarios

The standard tests folder includes the following test scenarios:

### Installation Tests
- **Purpose**: Verify that the Vector Databases can be accessed correctly and that the required dependencies are met.
- **Coverage**: Connection setup, configuration checks, and validation of access.

### Usage Tests
- **Purpose**: Ensure that the Vector Databases can be used correctly and that they return expected results.
- **Coverage**: Basic operations such as data insertion, retrieval, and simple queries.

### Basic Features
- **Purpose**: Validate that the basic features of the Vector Databases are functioning as expected.
- **Coverage**: Collection creation, basic search functionalities, and standard query operations.

## Using the Vector Databases

To use each Vector Database, you need to set up the appropriate environment variables and use the Vector Database Cloud API. Here are examples for each database:

### pgvector

```python
import os
import requests

API_URL = os.getenv('VECTORDBCLOUD_PGVECTOR_API_URL')
API_KEY = os.getenv('VECTORDBCLOUD_PGVECTOR_API_KEY')

# Use the API to interact with pgvector
```

### ChromaDB

```python
import os
import requests

API_URL = os.getenv('VECTORDBCLOUD_CHROMADB_API_URL')
API_KEY = os.getenv('VECTORDBCLOUD_CHROMADB_API_KEY')

# Use the API to interact with ChromaDB
```

### Milvus

```python
import os
import requests

API_URL = os.getenv('VECTORDBCLOUD_MILVUS_API_URL')
API_KEY = os.getenv('VECTORDBCLOUD_MILVUS_API_KEY')

# Use the API to interact with Milvus
```

### Qdrant

```python
import os
import requests

API_URL = os.getenv('VECTORDBCLOUD_QDRANT_API_URL')
API_KEY = os.getenv('VECTORDBCLOUD_QDRANT_API_KEY')

# Use the API to interact with Qdrant
```

## Troubleshooting

If you encounter issues:

1. Ensure all environment variables are correctly set.
2. Check your internet connection and API endpoint accessibility.
3. Verify that you have the correct permissions for the Vector Database Cloud services.
4. For specific error messages, refer to the documentation of the respective vector database or create an issue in this repository.


## Contribution and Feedback

We welcome contributions to expand these test scenarios. For contributing new tests or suggesting improvements, please refer to our [Contribution Guidelines](../CONTRIBUTING.md). If you encounter issues or have suggestions, please use the issue tracker.


## Disclaimer

These scripts are provided as examples and may need to be adapted to your specific use case and production environment. They are not guaranteed to work in all scenarios and should be thoroughly tested before use in any critical or production systems. Always follow best practices for security and performance when working with databases and APIs. The authors and contributors of this repository are not responsible for any damages or losses that may result from the use of these scripts.

Vector Database Cloud configurations may vary, and it's essential to consult the official documentation and your system administrators before running these tests in your environment. Ensure you have the necessary permissions and understand the potential impact of each operation on your data and system resources.
