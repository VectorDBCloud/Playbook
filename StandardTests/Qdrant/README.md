![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)
![Python](https://img.shields.io/badge/python-3.7%2B-green.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

# Standard Tests for Qdrant

This folder includes standard tests and example scripts for Qdrant, highlighting basic operations and setup within the Vector Database Cloud environment.

## Table of Contents

- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Test Scripts](#test-scripts)
- [Usage](#usage)
- [Troubleshooting](#troubleshooting)
- [Contribution and Feedback](#contribution-and-feedback)
- [Disclaimer](#disclaimer)

## Introduction

These tests are designed to verify the basic functionality of Qdrant when used with Vector Database Cloud. They cover operations from collection creation to data manipulation and searching.

## Prerequisites

- Python 3.7+
- `requests` library
- `pandas` library (for data import)
- `sentence_transformers` library (for embedding generation)
- Access to Vector Database Cloud with API URL and API key for Qdrant

Install the required libraries using:
```
pip install requests pandas sentence_transformers
```

## Test Scripts

- **CreatingCollections.py**: Creates collections in Qdrant.
- **Deletion.py**: Manages deletion operations for items or collections.
- **Deployment.py**: Demonstrates the deployment process for Qdrant instances.
- **Embedding.py**: Generates and uses embeddings.
- **ImportingData.py**: Imports data into Qdrant.
- **Search.py**: Executes search operations in Qdrant.

## Usage

1. Set up your environment variables:
   ```
   export VECTORDBCLOUD_QDRANT_API_URL="https://your-vector-db-cloud-url.com"
   export VECTORDBCLOUD_QDRANT_API_KEY="your-api-key"
   ```

2. Run each script individually:
   ```
   python <script_name>.py
   ```

3. Review the output to ensure operations were successful.

Each script is a practical example of operations you can perform with Qdrant. Read the script's internal documentation for detailed usage instructions.

## Troubleshooting

If you encounter issues:

1. Ensure all environment variables are correctly set.
2. Check your internet connection and API endpoint accessibility.
3. Verify that you have the correct permissions for the Vector Database Cloud services.
4. For specific error messages, refer to the Qdrant documentation or create an issue in this repository.


## Contribution and Feedback

We welcome contributions and feedback. Please follow our [Contribution Guidelines](../../CONTRIBUTING.md) and use the issue tracker for any issues or suggestions.


## Disclaimer

These scripts are provided as examples and may need to be adapted to your specific use case and production environment. They are not guaranteed to work in all scenarios and should be thoroughly tested before use in any critical or production systems. Always follow best practices for security and performance when working with databases and APIs. The authors and contributors of this repository are not responsible for any damages or losses that may result from the use of these scripts.

Vector Database Cloud and Qdrant configurations may vary, and it's essential to consult the official documentation and your system administrators before running these tests in your environment. Ensure you have the necessary permissions and understand the potential impact of each operation on your data and system resources.
