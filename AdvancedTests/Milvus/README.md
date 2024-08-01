# Advanced Tests for Milvus

This folder contains advanced test scenarios and usage examples for Milvus, focusing on complex operations and optimizations. These tests explore the advanced capabilities of Milvus and provide guidance on maximizing its performance and functionality.

## Introduction

The advanced tests for Milvus include scenarios such as performance benchmarking, handling complex queries, optimizing indexing strategies, and testing scalability. These scenarios are designed to evaluate the database's advanced features and to push its limits under various conditions.

## Test Scenarios

### Create a Collection with Custom Indexing
- **Purpose**: Demonstrates how to create collections with custom indexing strategies.
- **File**: `CreateACollectionWithCustomIndexing.py`

## Advanced Functions

### Searching
- **`milvus.advanced_search(query, vector_db)`**: Executes complex searches using detailed criteria.
  - **Example**: `milvus.advanced_search("deep learning applications", vector_db)`
  - **Returns**: A list of results matching the query.

### Insertion
- **`milvus.insert_advanced(vector, vector_db)`**: Inserts a vector into the database with advanced metadata.
  - **Example**: `milvus.insert_advanced([0.1, 0.5, 0.3], vector_db)`
  - **Returns**: The ID of the inserted vector.

### Update
- **`milvus.update_vector(vector_id, new_data, vector_db)`**: Updates an existing vector in the database.
  - **Example**: `milvus.update_vector(123, [0.2, 0.6, 0.4], vector_db)`
  - **Returns**: The ID of the updated vector.

### Deletion
- **`milvus.delete_vector(vector_id, vector_db)`**: Deletes a vector from the database.
  - **Example**: `milvus.delete_vector(123, vector_db)`
  - **Returns**: Confirmation of deletion.

## Contribution and Feedback

We welcome contributions to enhance these advanced test scenarios. Please refer to our Contribution Guidelines for more information. If you encounter any issues or have suggestions, please use the issue tracker.

## License

This content is licensed under the MIT License. See the LICENSE file for more details.
