![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)
![Python](https://img.shields.io/badge/python-3.7%2B-green.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

# Standard Tests for ChromaDB

This folder contains standard test scripts for ChromaDB, covering fundamental operations and setup processes.

## Table of Contents

- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Test Scripts](#test-scripts)
- [Usage](#usage)
- [Troubleshooting](#troubleshooting)
- [Contribution and Feedback](#contribution-and-feedback)
- [Disclaimer](#disclaimer)

## Introduction

These tests are designed to verify the basic functionality of ChromaDB when used with Vector Database Cloud. They cover operations from database and tenant creation to data manipulation and searching.

## Prerequisites

- Python 3.7+
- `requests` library
- `pandas` library (for data import)
- `sentence_transformers` library (for embedding generation)
- Access to Vector Database Cloud with API URL and API key for ChromaDB

Install the required libraries using:
```
pip install requests pandas sentence_transformers
```

## Test Scripts

- **CreateDatabase.py**: Creates a new database in ChromaDB.
- **CreateTenant.py**: Manages the creation of tenants within the database.
- **CreatingCollections.py**: Creates collections in ChromaDB.
- **Deletion.py**: Demonstrates deletion of records or collections.
- **Deployment.py**: Illustrates the deployment process for ChromaDB.
- **Embedding.py**: Generates and uses embeddings.
- **GetDatabase.py**: Retrieves database information.
- **GetTenant.py**: Fetches tenant details.
- **ImportingData.py**: Imports data into ChromaDB.
- **Search.py**: Demonstrates search functionality within ChromaDB.

## Usage

1. Set up your environment variables:
   ```
   export VECTORDBCLOUD_CHROMADB_API_URL="https://your-vector-db-cloud-url.com"
   export VECTORDBCLOUD_CHROMADB_API_KEY="your-api-key"
   ```

2. Run each script individually:
   ```
   python <script_name>.py
   ```

3. Review the output to ensure operations were successful.

## Troubleshooting

If you encounter issues:

1. Ensure all environment variables are correctly set.
2. Check your internet connection and API endpoint accessibility.
3. Verify that you have the correct permissions for the Vector Database Cloud services.
4. For specific error messages, refer to the ChromaDB documentation or create an issue in this repository.


## Contribution and Feedback

We appreciate contributions and feedback. Please refer to our [Contribution Guidelines](../../CONTRIBUTING.md) and report any issues or suggestions via the issue tracker.


## Disclaimer

These scripts are provided as examples and may need to be adapted to your specific use case and production environment. They are not guaranteed to work in all scenarios and should be thoroughly tested before use in any critical or production systems. Always follow best practices for security and performance when working with databases and APIs. The authors and contributors of this repository are not responsible for any damages or losses that may result from the use of these scripts.

Vector Database Cloud and ChromaDB configurations may vary, and it's essential to consult the official documentation and your system administrators before running these tests in your environment. Ensure you have the necessary permissions and understand the potential impact of each operation on your data and system resources.
