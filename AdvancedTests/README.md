# Advanced Tests

This folder contains a collection of advanced test scenarios for Vector Databases, focusing on complex functionalities and optimizations. These tests explore advanced use cases and push the capabilities of the databases.

## Introduction

The advanced tests cover scenarios beyond basic operations, including performance benchmarking, complex query handling, indexing strategies, and scalability testing. These tests help in understanding the limits and advanced features of the Vector Databases.

## Advanced Functions by Database

### pgvector

Advanced functions available for pgvector:

- **`pgvector.search(query, vector_db)`**: Searches for vectors in the database that match the query.
  - **Example**: `pgvector.search("hello world", vector_db)`
  - **Returns**: A list of vectors that match the query.

- **`pgvector.insert(vector, vector_db)`**: Inserts a new vector into the database.
  - **Example**: `pgvector.insert([1, 2, 3], vector_db)`
  - **Returns**: The ID of the newly inserted vector.

- **`pgvector.update(vector, vector_db)`**: Updates an existing vector in the database.
  - **Example**: `pgvector.update([1, 2, 3], vector_db)`
  - **Returns**: The ID of the updated vector.

- **`pgvector.delete(vector, vector_db)`**: Deletes a vector from the database.
  - **Example**: `pgvector.delete([1, 2, 3], vector_db)`
  - **Returns**: The ID of the deleted vector.

### ChromaDB

Advanced functions available for ChromaDB:

- **`chromadb.search(query, vector_db)`**: Searches for vectors in the database that match the query.
  - **Example**: `chromadb.search("hello world", vector_db)`
  - **Returns**: A list of vectors that match the query.

- **`chromadb.insert(vector, vector_db)`**: Inserts a new vector into the database.
  - **Example**: `chromadb.insert([1, 2, 3], vector_db)`
  - **Returns**: The ID of the newly inserted vector.

- **`chromadb.update(vector, vector_db)`**: Updates an existing vector in the database.
  - **Example**: `chromadb.update([1, 2, 3], vector_db)`
  - **Returns**: The ID of the updated vector.

- **`chromadb.delete(vector, vector_db)`**: Deletes a vector from the database.
  - **Example**: `chromadb.delete([1, 2, 3], vector_db)`
  - **Returns**: The ID of the deleted vector.

### Milvus

Advanced functions available for Milvus:

- **`milvus.search(query, vector_db)`**: Searches for vectors in the database that match the query.
  - **Example**: `milvus.search("hello world", vector_db)`
  - **Returns**: A list of vectors that match the query.

- **`milvus.insert(vector, vector_db)`**: Inserts a new vector into the database.
  - **Example**: `milvus.insert([1, 2, 3], vector_db)`
  - **Returns**: The ID of the newly inserted vector.

- **`milvus.update(vector, vector_db)`**: Updates an existing vector in the database.
  - **Example**: `milvus.update([1, 2, 3], vector_db)`
  - **Returns**: The ID of the updated vector.

- **`milvus.delete(vector, vector_db)`**: Deletes a vector from the database.
  - **Example**: `milvus.delete([1, 2, 3], vector_db)`
  - **Returns**: The ID of the deleted vector.

### Qdrant

Advanced functions available for Qdrant:

- **`qdrant.search(query, vector_db)`**: Searches for vectors in the database that match the query.
  - **Example**: `qdrant.search("hello world", vector_db)`
  - **Returns**: A list of vectors that match the query.

- **`qdrant.insert(vector, vector_db)`**: Inserts a new vector into the database.
  - **Example**: `qdrant.insert([1, 2, 3], vector_db)`
  - **Returns**: The ID of the newly inserted vector.

- **`qdrant.update(vector, vector_db)`**: Updates an existing vector in the database.
  - **Example**: `qdrant.update([1, 2, 3], vector_db)`
  - **Returns**: The ID of the updated vector.

- **`qdrant.delete(vector, vector_db)`**: Deletes a vector from the database.
  - **Example**: `qdrant.delete([1, 2, 3], vector_db)`
  - **Returns**: The ID of the deleted vector.

## Contribution and Feedback

We encourage contributions to enhance these advanced test scenarios. For contributing new tests or suggesting improvements, please refer to our [Contribution Guidelines](../CONTRIBUTING.md). If you encounter issues or have suggestions, please use the issue tracker.

## License

This repository is licensed under the MIT License. See the [LICENSE](../LICENSE) file for details.
