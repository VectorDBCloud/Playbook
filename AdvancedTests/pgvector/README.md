# Advanced Tests for pgvector

This folder contains advanced test scenarios and usage examples for pgvector, focusing on complex operations and optimizations. These tests explore the advanced capabilities of pgvector and provide guidance on maximizing its performance and functionality.

## Introduction

The advanced tests for pgvector include scenarios such as performance benchmarking, handling complex queries, optimizing indexing strategies, and testing scalability. These scenarios are designed to evaluate the database's advanced features and explore its limits under various conditions.

## Test Scenarios

### Create a Collection with Custom Indexing
- **Purpose**: Demonstrates how to create collections with custom indexing strategies.
- **File**: `CreateACollectionWithCustomIndexing.py`

### Search with Embeddings
- **Purpose**: Illustrates how to perform searches using vector embeddings for enhanced query accuracy.
- **File**: `SearchWithEmbeddings.py`

### Upsert with Custom Logic
- **Purpose**: Shows how to implement upsert operations with custom logic to manage vector data.
- **File**: `UpsertWithCustomLogic.py`

## Advanced Functions

### Searching
- **`pgvector.advanced_search(query, vector_db)`**: Performs complex searches using detailed criteria.
  - **Example**: `pgvector.advanced_search("advanced machine learning models", vector_db)`
  - **Returns**: A list of results matching the query.

### Insertion
- **`pgvector.insert_advanced(vector, vector_db)`**: Inserts a vector with additional metadata for advanced usage.
  - **Example**: `pgvector.insert_advanced([0.1, 0.5, 0.3], vector_db)`
  - **Returns**: The ID of the inserted vector.

### Update
- **`pgvector.update_vector(vector_id, new_data, vector_db)`**: Updates an existing vector in the database.
  - **Example**: `pgvector.update_vector(123, [0.2, 0.6, 0.4], vector_db)`
  - **Returns**: The ID of the updated vector.

### Deletion
- **`pgvector.delete_vector(vector_id, vector_db)`**: Deletes a vector from the database.
  - **Example**: `pgvector.delete_vector(123, vector_db)`
  - **Returns**: Confirmation of deletion.

## Contribution and Feedback

We welcome contributions to enhance these advanced test scenarios. Please refer to our Contribution Guidelines for more information. If you encounter any issues or have suggestions, please use the issue tracker.

## License

This content is licensed under the MIT License. See the LICENSE file for more details.
