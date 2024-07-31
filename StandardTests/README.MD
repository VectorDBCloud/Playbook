# Standard Tests

This folder contains a collection of standard tests for the Vector Databases, including installation instructions and examples of how to use each Vector Database.

## Introduction

The standard tests folder includes a variety of tests that cover different aspects of the Vector Databases, including installation, usage, and advanced features. These tests are designed to help you get started with using the Vector Databases and to provide a baseline for testing and validation.

## Test Scenarios

The standard tests folder includes the following test scenarios:

* Installation tests: These tests verify that the Vector Databases can be installed correctly and that the required dependencies are met.
* Usage tests: These tests verify that the Vector Databases can be used correctly and that the expected results are returned.
* Advanced tests: These tests verify that the advanced features of the Vector Databases are working correctly and that the expected results are returned.

## Using the Vector Databases

Once you have installed the Vector Databases, you can use them in your playground environment. Here are some examples of how to use each VectorDB:

### pgvector

To use pgvector, you'll need to create a new instance of the `pgvector` class and pass in the required parameters. Here's an example:
```python
import pgvector

vector_db = pgvector.PgVector( host='your_host', port=5432, database='your_database', username='your_username', password='your_password' )


##ChromaDB
To use chromadb, you'll need to create a new instance of the chromadb class and pass in the required parameters. Here's an example:

import chromadb

vector_db = chromadb.ChromeDB( host='your_host', port=5432, database='your_database', username='your_username', password='your_password' )


##Milvus
To use milvus, you'll need to create a new instance of the milvus class and pass in the required parameters. Here's an example:

import milvus

vector_db = milvus.Milvus( host='your_host', port=5432, database='your_database', username='your_username', password='your_password' )


##Qdrant
To use qdrant, you'll need to create a new instance of the qdrant class and pass in the required parameters. Here's an example:

import qdrant

vector_db = qdrant.Qdrant( host='your_host', port=5432, database='your_database', username='your_username', password='your_password' )
