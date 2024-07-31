# Standard Tests

This folder contains a collection of standard tests for the Vector Databases, including installation instructions and examples of how to use each Vector Database.

## Introduction

The standard tests folder includes a variety of tests that cover different aspects of the Vector Databases, including installation, usage, and basic features. These tests are designed to help you get started with using the Vector Databases and to provide a baseline for testing and validation.

## Test Scenarios

The standard tests folder includes the following test scenarios:

### Installation Tests
- **Purpose**: Verify that the Vector Databases can be installed correctly and that the required dependencies are met.
- **Coverage**: Installation steps, configuration checks, and validation of setup.

### Usage Tests
- **Purpose**: Ensure that the Vector Databases can be used correctly and that they return expected results.
- **Coverage**: Basic operations such as data insertion, retrieval, and simple queries.

### Basic Features
- **Purpose**: Validate that the basic features of the Vector Databases are functioning as expected.
- **Coverage**: Index creation, basic search functionalities, and standard query operations.

## Using the Vector Databases

Once you have installed the Vector Databases, you can use them in your development environment. Below are examples of how to use each Vector Database:

### pgvector

To use pgvector, initialize the database connection with the required parameters:

```
python
import pgvector

vector_db = pgvector.PgVector(
    host='your_host', 
    port=5432, 
    database='your_database', 
    username='your_username', 
    password='your_password'
)
```

### ChromaDB

To use ChromaDB, initialize the database connection with the required parameters:

```
import chromadb

vector_db = chromadb.ChromeDB(
    host='your_host', 
    port=5432, 
    database='your_database', 
    username='your_username', 
    password='your_password'
)
```

### Milvus
To use Milvus, initialize the database connection with the required parameters:

```
import milvus

vector_db = milvus.Milvus(
    host='your_host', 
    port=5432, 
    database='your_database', 
    username='your_username', 
    password='your_password'
)
```

### Qdrant
To use Qdrant, initialize the database connection with the required parameters:

```
import qdrant

vector_db = qdrant.Qdrant(
    host='your_host', 
    port=5432, 
    database='your_database', 
    username='your_username', 
    password='your_password'
)
```

### Contribution and Feedback
We welcome contributions to expand these test scenarios. For contributing new tests, please refer to our Contribution Guidelines. If you encounter issues or have suggestions, please use the issue tracker.
